from .heuristic import Heuristic


class CarAvailableMoves(Heuristic):
    """
    Like CarsInBetween, but also increases cost based on the number of cars blocking
    each car between the player and the exit.
    """

    @staticmethod
    def estimate(state):
        count = 0
        for i in range(state.player.y):
            car = state.car_in((state.exit, i))
            count += 1  # player movement to pass through this square

            if not car:
                continue

            count += 1  # must use at least one move to move a blocking car

            blockers = car.blocked_by
            if not blockers:
                continue

            # need to use at least one move per blocking car to free this one
            count += len(blockers)

        return count
