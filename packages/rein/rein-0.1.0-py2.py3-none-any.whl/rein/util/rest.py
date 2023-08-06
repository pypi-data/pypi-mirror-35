#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiohttp
import requests


async def async_fetch_json(url, *args, **kwargs):
    async with aiohttp.request('GET', url, *args, **kwargs) as r:
        data = await r.json()
    return data


def fetch_json(url, *args, **kwargs):
    r = requests.get(url, *args, **kwargs)
    return r.json()


if __name__ == '__main__':
    contracts = fetch_json(
        'https://1token.trade/api/v1/basic/contracts',
        params={'exchange': 'okex'})
    print(contracts)
