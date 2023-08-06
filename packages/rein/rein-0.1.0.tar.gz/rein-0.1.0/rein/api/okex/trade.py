#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import json
import os
import sys
import time
from enum import IntEnum

from bidict import bidict
from blinker import signal
from twisted.internet.ssl import ClientContextFactory
from twisted.web.client import Agent, readBody

from . import (OKEXWsClientFactory, OKEXWsClientProtocol, signed_rest_str,
               signed_ws_param)
from ..trade import *
from .error_code import REST_ERR_MAP


class OKEXOrderState(IntEnum):
    PENDING = 0
    WITHDRAWN = -1
    PART_DEAL_PENDING = 1  # TODO: to confirm if this state is final
    DEALT = 2
    WITHDRAWING = 4


ORDER_STATE_MAP = {
    OKEXOrderState.PENDING: OrderState.PENDING,
    OKEXOrderState.WITHDRAWN: OrderState.WITHDRAWN,
    OKEXOrderState.PART_DEAL_PENDING: OrderState.PART_DEAL_PENDING,
    OKEXOrderState.DEALT: OrderState.DEALT,
    OKEXOrderState.WITHDRAWING: OrderState.WITHDRAWING,
}


class WebClientContextFactory(ClientContextFactory):
    def getContext(self, hostname, port):
        return ClientContextFactory.getContext(self)


class TradeService(OKEXWsClientFactory):
    ORDER_FMT = 'ok_sub_spot_{}_order'
    BALANCE_FMT = 'ok_sub_spot_{}_balance'
    SUB_SIGNAL_FMT = 'okex_{}_{}'  # okex_[API_KEY]_[TradeInfoType]

    def __init__(self, tradeables, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tradeables = set(tradeables)
        self._url_base = 'https://www.okb.com/api/v1/'
        self._api_key = os.getenv('OKEX_API_KEY', None)
        self._secret_key = os.getenv('OKEX_SECRET_KEY', None)
        if not (self._api_key and self._secret_key):
            self.log.error(
                'API key or secret key not found, please set enviroment'
                ' variable OKEX_API_KEY and OKEX_SECRET_KEY'
            )
            sys.exit(-1)
        from twisted.internet import reactor
        self._rest_agent = Agent(reactor, WebClientContextFactory())
        self._query_userinfo()
        self._order_id_bidict = bidict()  # { order_id: outer_id }
        self._unbounded_orders = collections.defaultdict(
            list)  # {outer_id: [raw_order_msg] }
        self._order_id_symbol = {}
        self._unfinished_orders = {}  # {order_id: OrderInfo}
        self._balances = collections.defaultdict(
            tuple)  # {coin: (free, freeze)}

    def _query_userinfo(self):
        url = self._url_base + 'userinfo.do'
        params = {
            'api_key': self._api_key,
        }
        d = self._sign_and_request('POST', url, params)

        def on_body(msg):
            msg_info = json.loads(msg.decode('utf8'))
            raw_balance = msg_info['info']['funds']
            self._balances = self._handle_raw_balance(raw_balance)
            self.log.info('retrived balance: ')
            self.log.info(self._balances)
            self._fire_trade_info(
                TradeInfoType.ACCOUNT, AccountInfo(balances=self._balances))

        d.addCallback(lambda resp: readBody(resp).addCallback(on_body))

    def _sign_and_request(self, http_mothod, req_url, params):
        signed = signed_rest_str(params, self._secret_key)
        url = '{}?{}'.format(req_url, signed)
        d = self._rest_agent.request(
            http_mothod.encode('utf-8'), url.encode('utf-8'))
        return d

    def place_order(self, order_req, on_order_rep):
        """place order api(async function)

        :param order_req: type PlaceOrderReq or collection of PlaceOrderReqs
        :param on_order_rep: callback function to handle order rep

        :rtype: deferred
        """

        def place_single_order(order_req, on_order_rep):
            self.log.info('receive order req {}'.format(order_req))
            params = self._order_req2raw(order_req)
            d = self._sign_and_request('POST', url, params)
            order_info = self._order_req2order_info(order_req)
            self._unfinished_orders[order_req.order_id] = order_info
            self._fire_trade_info(TradeInfoType.ORDER, order_info)

            def on_resp(msg):
                # TODO: need to solve log_format error
                msg_info = json.loads(msg.decode('utf8'))
                order_info = self._unfinished_orders.get(
                    order_req.order_id, None)
                if msg_info.get('error_code', False):  # error occurs
                    err_code = repr(msg_info['error_code'])
                    err_msg = REST_ERR_MAP.get(err_code, None)
                    err_info = {'err_code': err_code, 'err_msg': err_msg}
                    rep = PlaceOrderRep(
                        exchange_ts=time.time(), error=err_info)
                    self.log.error(rep)
                    if order_info:
                        order_info.state = OrderState.ERROR
                        order_info.error_msg = err_msg
                        self._fire_trade_info(TradeInfoType.ORDER, order_info)
                    self._cleanup_finished_order(order_req.order_id)
                else:  # on success
                    outer_id = msg_info['order_id']
                    rep = PlaceOrderRep(
                        order_id=order_req.order_id, exchange_ts=time.time())
                    order_info.outer_order_id = outer_id
                    self.log.info('{} outer_id: {}'.format(rep, outer_id))
                    self._order_id_bidict[order_req.order_id] = outer_id
                    self._order_id_symbol[
                        order_req.order_id] = order_req.symbol
                    if outer_id in self._unbounded_orders:
                        for raw_order in self._unbounded_orders[outer_id]:
                            self._handle_raw_order(raw_order)
                        del self._unbounded_orders[outer_id]
                return rep

            d.addCallback(lambda resp: readBody(resp).addCallback(on_resp))
            d.addCallback(on_order_rep)
            d.addErrback(self.log.error)
            return d

        url = self._url_base + 'trade.do'
        if isinstance(order_req, collections.Iterable):
            for req in order_req:
                place_single_order(req, on_order_rep)
        else:
            place_single_order(order_req, on_order_rep)

    def withdraw_order(self, order_id, on_withdraw_rep):
        """withdraw order api(async function)

        :param order_id: order_id or collection of order_ids
        :param on_withdraw_rep: callback fucntion to handle withdraw rep

        """

        def withdraw_single_order(order_id, on_withdraw_rep):
            self.log.info('receive withdraw req {}'.format(order_id))
            if order_id not in self._order_id_bidict:
                self.log.warn(
                    'withdraw failed: order_id {} not existed'.format(
                        order_id))
                return
            if order_id not in self._order_id_symbol:
                self.log.warn(
                    'withdraw failed: can\'t query symbol by order_id {}'.
                    format(order_id))
                return
            params = {
                'api_key': self._api_key,
                'symbol': self._order_id_symbol[order_id],
                'order_id': self._order_id_bidict[order_id],
            }
            d = self._sign_and_request('POST', url, params)

            def on_resp(msg):
                msg_info = json.loads(msg.decode('utf8'))
                if msg_info.get('result', False):  # withdraw success
                    return WithdrawOrderRep(order_id=order_id)
                else:  # withdraw error
                    self.log.error(msg)
                    return WithdrawOrderRep(order_id=order_id, error=msg)

            d.addCallback(lambda resp: readBody(resp).addCallback(on_resp))
            d.addCallback(on_withdraw_rep)
            d.addErrback(self.log.error)

        url = self._url_base + 'cancel_order.do'
        if isinstance(order_id, collections.Iterable):
            for single_order_id in order_id:
                withdraw_single_order(single_order_id, on_withdraw_rep)
        else:
            withdraw_single_order(order_id, on_withdraw_rep)

    def sub_tradeinfo(self, tradeinfo_type, on_tradeinfo):
        """subscribe trade information

        :param tradeinfo_type: one of TradeInfoType
        :param on_tradeinfo: callback function to handle tradeinfo changes

        """
        signal(self.SUB_SIGNAL_FMT.format(
            self._api_key, tradeinfo_type)).connect(on_tradeinfo)

    def unsub_tradeinfo(self, tradeinfo_type, on_tradeinfo):
        """unsubscribe trade information

        :param tradeinfo_type: one of TradeInfoType
        :param on_tradeinfo: callback function to handle tradeinfo changes

        """
        signal(self.SUB_SIGNAL_FMT.format(
            self._api_key, tradeinfo_type)).disconnect(on_tradeinfo)

    def _fire_trade_info(self, tradeinfo_type, trade_info):
        signal(self.SUB_SIGNAL_FMT.format(self._api_key,
                                          tradeinfo_type)).send(trade_info)

    def _handle_raw_balance(self, raw_balance_msg):
        self.log.info('receive raw balance msg: {}'.format(raw_balance_msg))
        free = {
            coin: float(free)
            for coin, free in raw_balance_msg['free'].items()
            if float(free) != 0
        }
        freeze = {
            coin: float(freeze)
            for coin, freeze in raw_balance_msg['freezed'].items()
            if float(freeze) != 0
        }
        all_coins = set(list(free.keys()) + list(freeze.keys()))

        return {
            coin: {
                'free': free.get(coin, 0),
                'freezed': freeze.get(coin, 0)
            }
            for coin in all_coins
        }

    def _handle_raw_order(self, raw_order_msg):
        self.log.info('receive raw order msg: {}'.format(raw_order_msg))
        outer_id = raw_order_msg.get('orderId', None)
        order_id = self._order_id_bidict.inv.get(outer_id, None)
        order_info = self._unfinished_orders.get(order_id, None)
        if not order_info:
            self._unbounded_orders[outer_id].append(raw_order_msg)
        else:
            order_info.avg_deal_price = raw_order_msg.get('averagePrice', None)
            order_info.update_ts = time.time()
            order_info.order_ts = float(raw_order_msg.get('createdDate',
                                                          0)) / 1000.0
            order_info.deal_vol = raw_order_msg.get('completedTradeAmount',
                                                    None)
            order_info.last_deal_vol = raw_order_msg.get(
                'sigTradeAmount', None)
            order_info.last_deal_price = raw_order_msg.get(
                'sigTradePrice', None)
            order_info.state = ORDER_STATE_MAP.get(
                raw_order_msg.get('status', OrderState.ERROR))
            self._fire_trade_info(TradeInfoType.ORDER, order_info)
            if is_final_state(order_info.state):
                self._cleanup_finished_order(order_info.order_id)

    def _order_req2raw(self, order_req):
        return {
            'api_key': self._api_key,
            'symbol': order_req.symbol,
            'type': 'buy' if order_req.bs == BS.BUY else 'sell',
            'price': order_req.lmt_price,
            'amount': order_req.volume,
        }

    def _order_req2order_info(self, order_req):
        return OrderInfo(
            symbol=order_req.symbol,
            order_id=order_req.order_id,
            bs=order_req.bs,
            order_type=order_req.order_type,
            order_price=order_req.lmt_price,
            update_ts=time.time(),
            order_vol=order_req.volume,
            deal_vol=0,
            last_deal_vol=0,
            state=OrderState.CREATED,
        )

    def _cleanup_finished_order(self, order_id):
        self._order_id_bidict.pop(order_id, None)
        self._order_id_symbol.pop(order_id, None)
        self._unfinished_orders.pop(order_id, None)


class TradeProtocol(OKEXWsClientProtocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._channel_handlers = {
            'login': self._on_login,
            'order': self._on_order,
            'balance': self._on_balance,
        }

    def _on_open(self):
        super()._on_open()
        self._login()

    def _login(self):
        param = {
            'event': 'login',
            'parameters': {
                'api_key': self.factory._api_key
            }
        }
        param['parameters'] = signed_ws_param(param['parameters'],
                                              self.factory._secret_key)
        self.send_text(param)

    def _on_login(self, channel, msg):
        try:
            if msg['data']['result']:
                self.log.info('login OK.')
            else:
                self.log.critical('login failed msg: {}'.format(msg))
        except KeyError:
            self.log.critical('login failed msg: {}'.format(msg))

    def _on_order(self, channel, msg):
        raw_order = msg.get('data', None)
        if raw_order:
            self.factory._handle_raw_order(raw_order)

    def _on_balance(self, channel, msg):
        data = msg.get('data', None)
        if not data:
            return
        balance_info = data.get('info', None)
        balances = self.factory._handle_raw_balance(balance_info)
        self.factory._fire_trade_info(
            TradeInfoType.ACCOUNT, AccountInfo(balances=balances))


if __name__ == '__main__':
    from ...util.log import add_stream_handler
    add_stream_handler()

    from twisted.python import log
    observer = log.PythonLoggingObserver(loggerName='twisted')
    observer.start()

    url = 'wss://real.okex.com:10441/websocket'

    trade_srv = TradeService(['ltc_btc', 'btc_usdt'], url)
    trade_srv.protocol = TradeProtocol

    from twisted.internet import reactor
    reactor.connectSSL(trade_srv.host, trade_srv.port, trade_srv,
                       ClientContextFactory())

    order_req = PlaceOrderReq()
    order_req.symbol = 'ltc_btc'
    order_req.sector = Sector.SPOT
    order_req.bs = BS.SELL
    order_req.order_type = OrderType.LIMIT
    order_req.lmt_price = 0.012
    order_req.volume = 0.001
    order_req.order_id = uuid.uuid4()

    def on_order_info(order_info):
        print('=======================order_info============================')
        print(order_info)
        print('=======================order_info============================')

    def on_account_info(account_info):
        print('======================account_info===========================')
        print(account_info)
        print('======================account_info===========================')

    def on_order_resp(resp):
        print('=======================order_resp============================')
        print(resp)
        print('=======================order_resp============================')

    def on_withdraw_resp(resp):
        print('======================withdraw_resp===========================')
        print(resp)
        print('======================withdraw_resp===========================')

    trade_srv.sub_tradeinfo(TradeInfoType.ORDER, on_order_info)
    trade_srv.sub_tradeinfo(TradeInfoType.ACCOUNT, on_account_info)

    reactor.callLater(5, trade_srv.place_order, order_req, on_order_resp)
    reactor.callLater(10, trade_srv.withdraw_order, order_req.order_id,
                      on_withdraw_resp)

    reactor.run()
