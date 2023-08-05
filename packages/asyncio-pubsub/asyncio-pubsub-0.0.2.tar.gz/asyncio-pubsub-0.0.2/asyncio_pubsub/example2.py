import logging
import random
import sys

from aiohttp import web

from asyncio_pubsub.client import Client

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger('aiohttp.access').setLevel(logging.WARN)
logging.getLogger('asyncio_pubsub.batch').setLevel(logging.DEBUG)

app = web.Application()

client = Client(app)
topic = 'projects/rgames-portal2-sandbox/topics/testtopic'


async def add(num):
    string = str(num)

    future = await client.publish(topic, string.encode('utf-8'))

    return future


async def test(request):
    nonce = random.randint(1, 1000)

    fut = await add(nonce)

    await fut

    res = fut.result()

    return web.Response(text=res,status=200)


app.add_routes([
    web.route('GET', '/', test)
])

if __name__ == '__main__':
    web.run_app(app, port=8002, host='127.0.0.1')
