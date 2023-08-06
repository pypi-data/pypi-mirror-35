# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class PersistAPI(ABCMeta):
    @abstractmethod
    def load(self, key):
        """load

        :param str key:
        :rtype: bytes

        """
        pass

    @abstractmethod
    def store(self, key, value):
        """store

        :param str key:
        :param value key:

        """
        pass
