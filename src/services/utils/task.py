__author__ = 'melalonso'

from abc import ABCMeta, abstractmethod


class Task(metaclass=ABCMeta):
    @abstractmethod
    def exec(self):
        pass
