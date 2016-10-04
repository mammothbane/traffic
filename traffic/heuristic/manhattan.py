from .heuristic import Heuristic


class Manhattan(Heuristic):
    """A simple heuristic that computes the player's Manhattan distance from the goal."""

    @staticmethod
    def estimate(state):
        return state.player.y
