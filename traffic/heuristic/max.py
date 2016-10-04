from . import heuristics
from .heuristic import Heuristic


class Max(Heuristic):
    @staticmethod
    def estimate(state):
        return max([h.estimate(state) for h in heuristics.values()])
