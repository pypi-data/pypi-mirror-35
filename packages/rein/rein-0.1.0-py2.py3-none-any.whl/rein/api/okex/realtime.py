#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

import txaio
from blinker import signal
from dateutil import parser

from . import OKEXWsClientFactory, OKEXWsClientProtocol
from ..quote.master import DepthN


class RealtimeService(OKEXWsClientFactory):
    DEPTH_FMT = 'ok_sub_spot_{}_depth'
    DEAL_FMT = 'ok_sub_spot_{}_deals'
    SNAPSHOT_FMT = 'ok_sub_spot_{}_ticker'
    DEPTH_N_FMT = 'ok_sub_spot_{}_depth_{}'

    def sub_snapshot(self, symbols, on_snapshot_handler):
        self._connect_signal(self.SNAPSHOT_FMT, symbols, on_snapshot_handler)

    def unsub_snapshot(self, symbols, on_snapshot_handler):
        self._disconnect_signal(self.SNAPSHOT_FMT, symbols,
                                on_snapshot_handler)

    def sub_depth(self, symbols, on_depth_handler, depth_n=DepthN.D200):
        if depth_n == DepthN.D200:
            self._connect_signal(self.DEPTH_FMT, symbols, on_depth_handler)
        else:
            self._connect_signal(self.DEPTH_N_FMT, symbols, on_depth_handler,
                                 depth_n)

    def unsub_depth(self, symbols, on_depth_handler, depth_n=DepthN.D200):
        if depth_n == DepthN.D200:
            self._disconnect_signal(self.DEPTH_FMT, symbols, on_depth_handler)
        else:
            self._disconnect_signal(self.DEPTH_N_FMT, symbols,
                                    on_depth_handler, depth_n)

    def sub_transaction(self, symbols, on_transaction_handler):
        self._connect_signal(self.DEAL_FMT, symbols, on_transaction_handler)

    def unsub_transaction(self, symbols, on_transaction_handler):
        self._disconnect_signal(self.DEAL_FMT, symbols, on_transaction_handler)

    def _connect_signal(self, channel_format, symbols, handler, suffix=None):
        params = []
        for symbol in symbols:
            channel = self._join_channel(channel_format, symbol, suffix)
            if len(signal(channel).receivers) == 0:
                params.append({'event': 'addChannel', 'channel': channel})
                self.connected_channels.add(channel)
            signal(channel).connect(handler)
        self._send_text(params)
        self.log.info('add channels {}'.format(params))

    def _disconnect_signal(self, channel_format, symbols, handler,
                           suffix=None):
        params = []
        for symbol in symbols:
            channel = self._join_channel(channel_format, symbol, suffix)
            signal(channel).disconnect(handler)
            if len(signal(channel).receivers) == 0:
                params.append({'event': 'removeChannel', 'channel': channel})
                self.connected_channels.remove(channel)
        self._send_text(params)
        self.log.info('remove channels {}'.format(params))

    def _join_channel(self, channel_format, symbol, suffix):
        if suffix:
            return channel_format.format(symbol, suffix)
        else:
            return channel_format.format(symbol)

    def _send_text(self, params):
        if len(params) != 0:
            if self.proto_inst:
                self.proto_inst.send_text(params)


class RealtimeProtocol(OKEXWsClientProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._channel_handlers = {
            'depth': self._on_depth,
            'deals': self._on_deal,
            'ticker': self._on_snapshot,
            str(DepthN.D5.value): self._on_depth,
            str(DepthN.D10.value): self._on_depth,
            str(DepthN.D20.value): self._on_depth,
            'addChannel': self._on_addchannel,
            'removeChannel': self._on_rmchannel,
        }

    def _on_open(self):
        super()._on_open()
        params = []
        for channel in self.factory.connected_channels:
            params.append({'event': 'addChannel', 'channel': channel})
        self.send_text(params)

    def _on_addchannel(self, channel, msg):
        try:
            if msg['data']['result']:
                return
        except KeyError as exc:
            self.log.error(exc)
        self.log.error('add channel failed. channel: {} msg: {}'.format(
            channel, msg))

    def _on_rmchannel(self, channel, msg):
        pass

    def _on_depth(self, channel, msg):
        symbol = self._parse_symbol(channel)
        data = msg['data']
        try:
            depth = {
                'exchange_ts': data['timestamp'] / 1000.0,
                'local_ts': time.time(),
                'symbol': symbol,
                'depth': {
                    'ask': [
                        level_info
                        for level_info in self._level_data_gen(data, 'asks')
                    ],
                    'bid': [
                        level_info
                        for level_info in self._level_data_gen(data, 'bids')
                    ],
                },
            }
        except Exception as ex:
            self.log.error('convert depth error {}'.format(ex))
            return
        signal(channel).send(depth)

    def _on_deal(self, channel, msg):
        symbol = self._parse_symbol(channel)
        for record in msg['data']:
            try:
                deal = {
                    'exchange_ts':
                    time.mktime(parser.parse(record[3]).timetuple()),
                    'local_ts':
                    time.time(),
                    'symbol':
                    symbol,
                    'price':
                    float(record[1]),
                    'volume':
                    float(record[2]),
                }
            except KeyError as ex:
                self.log.error('convert deal error {}'.format(ex))
                continue
            signal(channel).send(deal)

    def _on_snapshot(self, channel, msg):
        symbol = self._parse_symbol(channel)
        data = msg['data']
        try:
            snapshot = {
                'exchange_ts': data['timestamp'] / 1000.0,
                'local_ts': time.time(),
                'symbol': symbol,
                'price': {
                    1: float(data['sell']),
                    -1: float(data['buy']),
                },
                'change': float(data['change']),
            }
        except Exception as ex:
            self.log.error('convert snapshot error {}'.format(ex))
            return
        signal(channel).send(snapshot)

    def _level_data_gen(self, data, ok_side):
        for level_data in data[ok_side]:
            price = float(level_data[0])
            volume = float(level_data[1])
            yield (price, volume)


if __name__ == '__main__':

    def on_msg(msg):
        print(msg)
        # pass

    # from ...util.log import add_stream_handler, add_file_handler
    # add_stream_handler()
    # add_file_handler('okex_trade')
    txaio.start_logging(level='info')

    url = 'wss://real.okex.com:10441/websocket'
    quote_srv = RealtimeService(url)
    quote_srv.protocol = RealtimeProtocol

    from ..onetoken.master import MasterService

    master = MasterService()
    symbols = [
        '_'.join(symbol.split('.'))
        for symbol in master.get_available_symbols()
    ]
    # symbols = ['btc_usdt']

    from twisted.internet import reactor, ssl
    txaio.call_later(5, quote_srv.sub_depth, symbols, on_msg, DepthN.D200)
    # txaio.call_later(1, quote_srv.sub_transaction, symbols, on_msg)
    # txaio.call_later(1, quote_srv.sub_snapshot, symbols, on_msg)

    reactor.connectSSL(quote_srv.host, quote_srv.port, quote_srv,
                       ssl.ClientContextFactory())
    reactor.run()
