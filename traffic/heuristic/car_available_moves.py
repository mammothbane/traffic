from .heuristic import Heuristic


class CarAvailableMoves(Heuristic):
    @staticmethod
    def estimate(state):
        count = 0
        for i in range(state.player.y):
            car = state.car_in((state.exit, i))
            count += 1

            if not car:
                continue

            count += 1

            blockers = car.blocked_by
            if not blockers:
                continue

            count += len(blockers)

        return count
