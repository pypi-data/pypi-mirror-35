#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ContractAPI.register
import asyncio

from ...util.rest import fetch_json
from ..quote.master import Contract, Sector


class MasterService:
    def __init__(self,
                 exchange='okex',
                 url='https://1token.trade/api/v1/basic/contracts'):
        contract_json = fetch_json(url, params={'exchange': exchange})
        self._contracts = {}
        for record in contract_json:
            symbol = record['name']
            contract = Contract(symbol, exchange, Sector.SPOT,
                                record['min_change'], record['unit_amount'],
                                record['min_amount'], record['currency'])
            self._contracts[symbol] = contract

    def get_available_symbols(self):
        yield from self._contracts.keys()

    def fetch_contract_info(self, symbol):
        if symbol not in self._contracts:
            return None
        return self._contracts[symbol]


if __name__ == '__main__':
    master = MasterService('okex')
    gen = master.get_available_symbols()
    for _ in range(3):
        symbol = next(gen)
        print(symbol)
        print(master.fetch_contract_info(symbol))
