# -*- coding: utf-8 -*-
import abc


class Serializable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def deserialize(self, stream):
        """deserialize from bytes

        :param bytes stream:

        """
        pass

    @abc.abstractmethod
    def serialize(self):
        """serialize to bytes

        :rtype: bytes

        """
        pass
