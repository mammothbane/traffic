from abc import ABCMeta, abstractmethod

from .puzzle import Puzzle
from .car import Car


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def step(self, puzzle):
        pass
