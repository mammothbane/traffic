from .heuristic import Heuristic


class Manhattan(Heuristic):
    @staticmethod
    def estimate(state):
        return state.player.y / state.config.dimens[1]
