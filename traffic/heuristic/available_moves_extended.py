from .heuristic import Heuristic


class AvailableMovesExtended(Heuristic):
    """
    Extends CarAvailableMoves by building a graph of all cars between the player and the exit
    that can't move at all, and increments cost based on the minimum number of moves that would be
    required to put them in a non-blocked state.
    """

    @staticmethod
    def estimate(state):
        count = 0
        for i in range(state.player.y):
            car = state.car_in((state.exit, i))
            count += 1

            if not car:
                continue

            count += 1
            count += AvailableMovesExtended.check_blockers(car, set())

        return count

    @staticmethod
    def check_blockers(car, seen):
        seen.add(car)
        new_blk = car.blocked_by
        if not new_blk:
            return 0

        return 1 + sum(AvailableMovesExtended.check_blockers(x, seen) for x in new_blk if x not in seen)
