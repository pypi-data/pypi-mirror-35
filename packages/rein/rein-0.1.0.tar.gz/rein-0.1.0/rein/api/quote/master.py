# -*- coding: utf-8 -*-
import abc
from enum import Enum, IntEnum

from namedlist import namedlist

from ...util.model import Typed


class Area(IntEnum):
    CHINA = 1
    USA = 2
    HONGKONG = 3
    JAPAN = 4
    SINGAPORE = 5
    UK = 6
    FRANCE = 7
    GERMAN = 8


class Period(IntEnum):
    YEAR = 1
    MONTH = 2
    WEEK = 3
    DAY = 4
    HOUR = 5
    MINUTES = 6
    SECONDS = 7
    MILLISECS = 8
    QUARTER = 9


class AdjustType(IntEnum):
    PRE = 1
    POST = 2
    NONE = 3


class Sector(Enum):
    SPOT = 'spot'
    FUTURE = 'future'
    OPTION = 'option'
    FX = 'fx'
    INDEX = 'index'
    BOND = 'bond'


class Side(Enum):
    ASK = 'ask'
    BID = 'bid'


class DepthN(IntEnum):
    D5 = 5
    D10 = 10
    D20 = 20
    D200 = 200


class SectorDes(Typed):
    expected_type = Sector


Contract = namedlist(
    'Contract', [
        'symbol', 'exchange', 'sector', 'price_tick', 'size_tick', 'min_size',
        'currency'
    ],
    default=None)


class TradingCalendarAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_calendar(self, area, begin, end):
        pass

    @abc.abstractmethod
    def is_tradingday(self):
        pass


class ContractAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_available_symbols(self):
        pass

    @abc.abstractmethod
    def fetch_contract_info(self, symbol):
        pass


class FundamentalAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_rf(self, freq):
        pass

    @abc.abstractmethod
    def fetch_deposit_rate(self, freq):
        pass

    @abc.abstractmethod
    def fetch_loan_rate(self, freq):
        pass

    @abc.abstractmethod
    def fetch_money_supply(self, freq):
        pass

    @abc.abstractmethod
    def fetch_gdp(self, freq):
        pass

    @abc.abstractmethod
    def fetch_cpi(self, freq):
        pass
