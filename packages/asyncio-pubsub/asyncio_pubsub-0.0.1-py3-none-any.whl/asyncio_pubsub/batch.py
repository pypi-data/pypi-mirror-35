import asyncio
import time

import google
import logging
from typing import List
from async_timeout import timeout

from google.cloud.pubsub_v1.publisher.batch.base import Batch
from google.cloud.pubsub_v1.publisher.batch import base

_CAN_COMMIT = (
    base.BatchStatus.ACCEPTING_MESSAGES,
    base.BatchStatus.STARTING,
)

_LOGGER = logging.getLogger('asyncio_pubsub.batch')

# https://github.com/GoogleCloudPlatform/google-cloud-python/tree/master/pubsub/google/cloud/pubsub_v1/publisher/_batch


class AsyncBatch(Batch):

    def __init__(self, app, client, topic, settings, autocommit=True):
        self._client = client
        self._topic = topic
        self._settings = settings
        self._app = app
        self._loop = asyncio.get_event_loop()

        self._queue = asyncio.Queue()
        self._messages = []
        self._size = 0
        self._status = base.BatchStatus.ACCEPTING_MESSAGES
        self._futures = []
        self._state_lock = asyncio.Lock()
        self.add_poller_to_app(app)

    def add_poller_to_app(self, app):
        app['poller'] = self._loop.create_task(self.poller())

    @staticmethod
    def make_lock():
        return asyncio.Lock()

    @property
    def messages(self):
        return self._messages

    @property
    def size(self):
        return self._size

    @property
    def settings(self):
        return self._settings

    @property
    def status(self):
        return self._status

    def will_accept(self, message):
        return super().will_accept(message)

    async def publish(self, message):
        future = asyncio.Future()
        await self._queue.put((future, message))
        return future

    async def poller(self):
        #size_limit = 10 #MB
        count_limit = 500
        time_limit = 0.05
        try:
            while True:
                try:
                    #size = 0
                    messages = []
                    futures: List[asyncio.Future] = []

                    logging.info('Waiting for messages...')
                    i = await self._queue.get()
                    future = i[0]
                    msg = i[1]

                    logging.info('Got message. Starting countdown')

                    #size += msg.ByteSize()
                    messages.append(msg)
                    futures.append(future)

                    while len(messages) < count_limit:
                        try:
                            async with timeout(time_limit):
                                i = await self._queue.get()
                        except asyncio.TimeoutError:
                            # Normal behavior
                            break
                        future = i[0]
                        msg = i[1]

                        #size += msg.ByteSize()
                        messages.append(msg)
                        futures.append(future)

                    await self._send(messages, futures)


                except asyncio.CancelledError:
                    raise
                except Exception as err:
                    logging.exception('Something went wrong')

        except asyncio.CancelledError:
            pass

    async def _send(self, messages, futures):
        logging.info('Got %s messages to send', len(messages))

        start = time.time()
        try:
            response = await self._loop.run_in_executor(None, self._client.api.publish, self._topic, messages)
            #response = self._client.api.publish(
            #    self._topic,
            #    messages,
            #)
        except google.api_core.exceptions.GoogleAPICallError as exc:
            # We failed to publish, set the exception on all futures and
            # exit.
            self._status = base.BatchStatus.ERROR

            for future in futures:
                future.set_exception(exc)

            _LOGGER.exception(
                'Failed to publish %s messages.', len(futures))
            return

        end = time.time()
        _LOGGER.debug('gRPC Publish took %s seconds.', end - start)

        if len(response.message_ids) == len(futures):
            # Iterate over the futures on the queue and return the response
            # IDs. We are trusting that there is a 1:1 mapping, and raise
            # an exception if not.
            zip_iter = zip(response.message_ids, futures)
            for message_id, future in zip_iter:
                if not future.cancelled():
                    future.set_result(message_id)
        else:
            # Sanity check: If the number of message IDs is not equal to
            # the number of futures I have, then something went wrong.
            exception = ValueError(
                'Some messages were not successfully published.')

            for future in futures:
                if not future.cancelled():
                    future.set_exception(exception)

            _LOGGER.error(
                'Only %s of %s messages were published.',
                len(response.message_ids), len(futures))

        for _ in futures:
            self._queue.task_done()
