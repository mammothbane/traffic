from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    def __init__(self, puzzle):
        self._puzzle = puzzle

    @abstractmethod
    def start(self):
        pass
