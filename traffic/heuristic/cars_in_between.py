from .heuristic import Heuristic


class CarsInBetween(Heuristic):
    @staticmethod
    def estimate(state):
        count = 0
        for i in range(state.player.y):
            count += 1
            if state.car_in((state.exit, i)):
                count += 1

        return count
