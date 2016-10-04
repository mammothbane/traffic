from .car_available_moves import CarAvailableMoves
from .cars_in_between import CarsInBetween
from .manhattan import Manhattan
from .max import Max

heuristics = {
    'cars_in_between': CarsInBetween,
    'manhattan': Manhattan,
    'max': Max,
    'car_available_moves': CarAvailableMoves,
}
