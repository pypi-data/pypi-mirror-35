import asyncio
import json

from ...util.rest import async_fetch_json


def on_coin_list(task):
    data = task.result()
    print(data['Data'])

if __name__ == '__main__':
    task = asyncio.ensure_future(
        async_fetch_json('https://www.cryptocompare.com/api/data/coinlist/'))
    task.add_done_callback(on_coin_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
