__author__ = 'melalonso'

from abc import ABCMeta, abstractmethod


class OutputMaker(metaclass=ABCMeta):
    @abstractmethod
    def make(self):
        pass
