# Copyright 2017, Google LLC All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from asyncio_pubsub.batch import AsyncBatch

import copy
import os
import pkg_resources

import grpc
import six

from google.api_core import grpc_helpers

from google.cloud.pubsub_v1 import _gapic
from google.cloud.pubsub_v1 import types
from google.cloud.pubsub_v1.gapic import publisher_client
from google.cloud.pubsub_v1.publisher.batch import thread


__version__ = pkg_resources.get_distribution('google-cloud-pubsub').version


@_gapic.add_methods(publisher_client.PublisherClient, blacklist=('publish',))
class Client(object):
    """A publisher client for Google Cloud Pub/Sub.

    This creates an object that is capable of publishing messages.
    Generally, you can instantiate this client with no arguments, and you
    get sensible defaults.

    Args:
        batch_settings (~google.cloud.pubsub_v1.types.BatchSettings): The
            settings for batch publishing.
        batch_class (Optional[Type]): A class that describes how to handle
            batches. You may subclass the
            :class:`.pubsub_v1.publisher.batch.base.BaseBatch` class in
            order to define your own batcher. This is primarily provided to
            allow use of different concurrency models; the default
            is based on :class:`threading.Thread`. This class should also have
            a class method (or static method) that takes no arguments and
            produces a lock that can be used as a context manager.
        kwargs (dict): Any additional arguments provided are sent as keyword
            arguments to the underlying
            :class:`~.gapic.pubsub.v1.publisher_client.PublisherClient`.
            Generally, you should not need to set additional keyword arguments.
            Before being passed along to the GAPIC constructor, a channel may
            be added if ``credentials`` are passed explicitly or if the
            Pub / Sub emulator is detected as running.
    """
    def __init__(self, app, batch_settings=(), batch_class=AsyncBatch, **kwargs):
        # Sanity check: Is our goal to use the emulator?
        # If so, create a grpc insecure channel with the emulator host
        # as the target.
        if os.environ.get('PUBSUB_EMULATOR_HOST'):
            kwargs['channel'] = grpc.insecure_channel(
                target=os.environ.get('PUBSUB_EMULATOR_HOST'),
            )

        # Use a custom channel.
        # We need this in order to set appropriate default message size and
        # keepalive options.
        if 'channel' not in kwargs:
            kwargs['channel'] = grpc_helpers.create_channel(
                credentials=kwargs.pop('credentials', None),
                target=self.target,
                scopes=publisher_client.PublisherClient._DEFAULT_SCOPES,
                options={
                    'grpc.max_send_message_length': -1,
                    'grpc.max_receive_message_length': -1,
                }.items(),
            )

        # Add the metrics headers, and instantiate the underlying GAPIC
        # client.
        self.api = publisher_client.PublisherClient(**kwargs)
        self.batch_settings = types.BatchSettings(*batch_settings)

        # The batches on the publisher client are responsible for holding
        # messages. One batch exists for each topic.
        self._batch_class = batch_class
        self._batch_lock = batch_class.make_lock()
        self._batches = {}
        self.app = app

    @property
    def target(self):
        """Return the target (where the API is).

        Returns:
            str: The location of the API.
        """
        return publisher_client.PublisherClient.SERVICE_ADDRESS

    async def batch(self, topic, create=False, autocommit=True):
        """Return the current batch for the provided topic.

        This will create a new batch if ``create=True`` or if no batch
        currently exists.

        Args:
            topic (str): A string representing the topic.
            create (bool): Whether to create a new batch. Defaults to
                :data:`False`. If :data:`True`, this will create a new batch
                even if one already exists.
            autocommit (bool): Whether to autocommit this batch. This is
                primarily useful for debugging and testing, since it allows
                the caller to avoid some side effects that batch creation
                might have (e.g. spawning a worker to publish a batch).

        Returns:
            ~.pubsub_v1.batch.Batch: The batch object.
        """
        # If there is no matching batch yet, then potentially create one
        # and place it on the batches dictionary.
        async with self._batch_lock:
            if not create:
                batch = self._batches.get(topic)
                if batch is None:
                    create = True

            if create:
                batch = self._batch_class(
                    app=self.app,
                    autocommit=autocommit,
                    client=self,
                    settings=self.batch_settings,
                    topic=topic,
                )
                self._batches[topic] = batch

        return batch

    async def publish(self, topic, data, **attrs):
        """Publish a single message.

        .. note::
            Messages in Pub/Sub are blobs of bytes. They are *binary* data,
            not text. You must send data as a bytestring
            (``bytes`` in Python 3; ``str`` in Python 2), and this library
            will raise an exception if you send a text string.

            The reason that this is so important (and why we do not try to
            coerce for you) is because Pub/Sub is also platform independent
            and there is no way to know how to decode messages properly on
            the other side; therefore, encoding and decoding is a required
            exercise for the developer.

        Add the given message to this object; this will cause it to be
        published once the batch either has enough messages or a sufficient
        period of time has elapsed.

        Example:
            >>> from google.cloud.pubsub_v1 import publisher_client
            >>> client = publisher_client.PublisherClient()
            >>> topic = client.topic_path('[PROJECT]', '[TOPIC]')
            >>> data = b'The rain in Wales falls mainly on the snails.'
            >>> response = client.publish(topic, data, username='guido')

        Args:
            topic (str): The topic to publish messages to.
            data (bytes): A bytestring representing the message body. This
                must be a bytestring.
            attrs (Mapping[str, str]): A dictionary of attributes to be
                sent as metadata. (These may be text strings or byte strings.)

        Returns:
            ~concurrent.futures.Future: An object conforming to the
            ``concurrent.futures.Future`` interface.
        """
        # Sanity check: Is the data being sent as a bytestring?
        # If it is literally anything else, complain loudly about it.
        if not isinstance(data, six.binary_type):
            raise TypeError(
                'Data being published to Pub/Sub must be sent '
                'as a bytestring.'
            )

        # Coerce all attributes to text strings.
        for k, v in copy.copy(attrs).items():
            if isinstance(v, six.text_type):
                continue
            if isinstance(v, six.binary_type):
                attrs[k] = v.decode('utf-8')
                continue
            raise TypeError(
                'All attributes being published to Pub/Sub must '
                'be sent as text strings.'
            )

        # Create the Pub/Sub message object.
        message = types.PubsubMessage(data=data, attributes=attrs)

        # Delegate the publishing to the batch.
        batch = await self.batch(topic)
        future = None
        while future is None:
            future = await batch.publish(message)
            if future is None:
                batch = self.batch(topic, create=True)

        return future