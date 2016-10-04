from itertools import count

from .dfs import DFS
from .strategy import Strategy


class IDS(Strategy):
    """
    Iterative deepening search, using the existing DFS implementation.

    If refactored somewhat, this could be optimized in a similar way as BFS, potentially by
    storing a dict mapping depth -> set of skippable states, but I don't feel a need
    to demonstrate that again. It functions on the 'simple' 4x4 puzzle but takes over an hour
    to search example 1 (depth 12, 16,180,312+ steps).
    """

    def __init__(self, puzzle):
        super().__init__(puzzle)
        self._init_state = puzzle.simple_cpy()
        self._dfs = DFS(puzzle)

    def start(self):
        for i in count():
            self._puzzle.use_cars(self._init_state)

            print('depth %s' % i)
            ok, s = self._dfs.start(i)
            if ok:
                print('optimal solution found at depth %s' % s.depth)
                break
