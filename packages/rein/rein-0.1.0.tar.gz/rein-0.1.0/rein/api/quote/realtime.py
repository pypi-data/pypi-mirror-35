# -*- coding: utf-8 -*-

import abc


class QuoteAPI(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sub_snapshot(self, symbols, on_snapshot_handler):
        pass

    @abc.abstractmethod
    def unsub_snapshot(self, symbols, on_snapshot_handler):
        pass

    @abc.abstractmethod
    def sub_depth(self, symbols, on_depth_handler):
        pass

    @abc.abstractmethod
    def unsub_depth(self, symbols, on_depth_handler):
        pass

    @abc.abstractmethod
    def sub_transaction(self, symbols, on_transaction_handler):
        pass

    @abc.abstractmethod
    def unsub_transaction(self, symbols, on_transaction_handler):
        pass
