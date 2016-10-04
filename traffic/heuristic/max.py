from .car_available_moves import CarAvailableMoves
from .cars_in_between import CarsInBetween
from .heuristic import Heuristic
from .manhattan import Manhattan


class Max(Heuristic):
    @staticmethod
    def estimate(state):
        return max([h.estimate(state) for h in [CarAvailableMoves, CarsInBetween, Manhattan]])
