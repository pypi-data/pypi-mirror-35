import asyncio
import logging
import random
import sys
from typing import List

from aiohttp import web
from google.cloud.pubsub_v1 import types
from async_timeout import timeout

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger('aiohttp.access').setLevel(logging.WARN)

app = web.Application()

queue = asyncio.Queue()

async def message_sender():
    #size_limit = 10 #MB
    count_limit = 800
    time_limit = 0.05
    try:
        while True:
            try:
                #size = 0
                messages: List[types.PubsubMessage] = []
                futures: List[asyncio.Future] = []

                logging.info('Waiting for messages...')
                i = await queue.get()
                future = i[0]
                msg = i[1]

                logging.info('Got message. Starting countdown')

                #size += msg.ByteSize()
                messages.append(msg)
                futures.append(future)

                while len(messages) < count_limit:
                    try:
                        async with timeout(time_limit):
                            i = await queue.get()
                    except asyncio.TimeoutError:
                        # Normal behavior
                        break
                    future = i[0]
                    msg = i[1]

                    #size += msg.ByteSize()
                    messages.append(msg)
                    futures.append(future)


                logging.info('Got %s messages to send', len(messages))

                await asyncio.sleep(0.1)

                for f in futures:
                    queue.task_done()
                    if not f.cancelled():
                        f.set_result('ok')
            except asyncio.CancelledError:
                raise
            except Exception as err:
                logging.exception('Something went wrong')

    except asyncio.CancelledError:
        pass

async def runner(app):
    app['poller'] = app.loop.create_task(message_sender())

async def stop(app):
    task = app['poller']

    if task:
        task.cancel()
        await task


app.on_startup.append(runner)
app.on_cleanup.append(stop)

async def add(num):
    future = asyncio.Future()

    await queue.put((future, num))

    return future


async def test(request):
    nonce = random.randint(1, 1000)

    fut = await add(nonce)

    #fut = asyncio.ensure_future(fut)

    #request.loop.run_until_complete(fut)
    await fut
    #logging.info('post fut')

    res = fut.result()

    #logging.info(res)

    return web.Response(text=res,status=200)


app.add_routes([
    web.route('GET', '/', test)
])

if __name__ == '__main__':
    web.run_app(app, port=8002, host='127.0.0.1')
