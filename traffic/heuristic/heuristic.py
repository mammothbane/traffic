from abc import ABCMeta, abstractstaticmethod


class Heuristic(metaclass=ABCMeta):
    @abstractstaticmethod
    def estimate(state):
        pass
