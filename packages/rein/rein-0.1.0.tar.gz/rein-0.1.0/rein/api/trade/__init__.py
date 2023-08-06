# -*- coding: utf-8 -*-
import abc
from enum import IntEnum

from namedlist import namedlist

from ...util.model import *
from ..quote.master import Sector


class SectorDes(Typed):
    expected_type = Sector


class BS(IntEnum):
    BUY = 1
    SELL = 2


class BSDes(Typed):
    expected_type = BS


class OC(IntEnum):
    OPEN = 1
    CLOSE = 2


class OCDes(Typed):
    expected_type = OC


class OrderLevel(IntEnum):
    LAST = 0
    LIMIT_UP = 9999
    LIMIT_DOWN = -9999


class OrderLevelDes(Typed):
    expected_type = OrderLevel


class OrderType(IntEnum):
    LIMIT = 1
    MARKET = 2


class OrderTypeDes(Typed):
    expected_type = OrderType


class OrderState(IntEnum):
    CREATED = 1
    PENDING = 2
    PART_DEAL_PENDING = 3
    WITHDRAWING = 4
    PART_DEAL_WITHDRAWING = 5
    WITHDRAWN = 6
    PART_DEAL_WITHDRAWN = 7
    DEALT = 8
    ERROR = 9


_final_state = set([
    OrderState.WITHDRAWN,
    OrderState.PART_DEAL_WITHDRAWN,
    OrderState.DEALT,
    OrderState.ERROR,
])


def is_final_state(order_state):
    return order_state in _final_state


class OrderStateDes(Typed):
    expected_type = OrderState


class TimeInForce(IntEnum):
    DAY = 1
    GTC = 2  # good until canceled
    IOC = 3  # immediate or cancel
    GTD = 4  # good until date
    FOK = 5  # fill-or-kill


class TimeInForceDes(Typed):
    expected_type = OrderState


class TradeInfoType(IntEnum):
    ACCOUNT = 1
    POSITION = 2
    ORDER = 3
    TRANSACTION = 4


class PlaceOrderReq(metaclass=checkedmeta):
    symbol = String('symbol')
    sector = SectorDes('sector')
    bs = BSDes('bs')
    oc = OCDes('oc')
    order_type = OrderTypeDes('order_type')
    lmt_price = Float('lmt_price')
    volume = Float('volume')
    tif = TimeInForceDes('tif')
    order_id = UUID('order_id')
    strategy_id = UUID('strategy_id')

    def __repr__(self):
        return '[PlaceOrderReq]\nsymbol: {0}\nbs: {1}\nprice: {2}\nvolume: {3}'.format(
            self.symbol, self.bs, self.lmt_price, self.volume)


PlaceOrderRep = namedlist(
    'PlaceOrderRep', ['order_id', 'exchange_ts', 'error'], default=None)
# WithdrawOrderReq = namedlist('WithdrawOrderReq', ['order_id'], default=None)
WithdrawOrderRep = namedlist(
    'WithdrawOrderRep', ['order_id', 'error'], default=None)

AccountInfo = namedlist(
    'AccountInfo', [
        'balances',
        'market_value',
        'net_liquidation',
        'realized_pnl',
        'unrealized_pnl',
        'leverage',
        'init_margin',
        'maint_margin',
    ],
    default=None)

OrderInfo = namedlist(
    'OrderInfo', [
        'symbol',
        'order_id',
        'outer_order_id',
        'bs',
        'order_type',
        'order_price',
        'avg_deal_price',
        'update_ts',
        'order_ts',
        'order_vol',
        'deal_vol',
        'last_deal_vol',
        'last_deal_price',
        'state',
        'oc',
        'error_msg',
    ],
    default=None)

TransactionInfo = namedlist(
    'TransactionInfo', [
        'symbol',
        'order_id',
        'transaction_no',
        'bs',
        'commission',
        'deal_vol',
        'deal_price',
        'deal_ts',
        'outer_order_id',
        'oc',
    ],
    default=None)

PositionInfo = namedlist(
    'PositionInfo', [
        'symbol',
        'bs',
        'volume',
        'avg_cost',
        'market_value',
        'realized_pnl',
        'unrealized_pnl',
    ],
    default=None)


class TradeAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def place_order(self, order_req, on_order_rep):
        """place order api(async function)

        :param order_req: type PlaceOrderReq or collection of PlaceOrderReqs
        :param on_order_rep: callback function to handle order rep

        """
        pass

    @abc.abstractmethod
    def withdraw_order(self, order_id, on_withdraw_rep):
        """withdraw order api(async function)

        :param order_id: order_id or collection of order_ids
        :param on_withdraw_rep: callback fucntion to handle withdraw rep

        """
        pass

    @abc.abstractmethod
    def sub_tradeinfo(self, tradeinfo_type, on_tradeinfo):
        """subscribe trade information

        :param tradeinfo_type: one of TradeInfoType
        :param on_tradeinfo: callback function to handle tradeinfo changes

        """
        pass

    @abc.abstractmethod
    def unsub_tradeinfo(self, tradeinfo_type, on_tradeinfo):
        """unsubscribe trade information

        :param tradeinfo_type: one of TradeInfoType
        :param on_tradeinfo: callback function to handle tradeinfo changes

        """
        pass
