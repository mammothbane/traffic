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

    def start(self):
        dfs = DFS(self._config)

        for i in count():
            print('depth %s' % i)
            ok, s = dfs.start(i)
            if ok:
                print('optimal solution found at depth %s' % s.depth)
                break
