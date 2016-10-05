from itertools import count

from .dfs import DFS
from .strategy import Strategy


class IDS(Strategy):
    """
    Iterative deepening search, using the existing DFS implementation.
    """

    def start(self):
        dfs = DFS(self._config)

        visited = 0

        for i in count():
            print('depth %s' % i)
            ok, s, ct = dfs.start(i, p=False)
            visited += ct

            if ok:
                print('optimal solution found at depth %s after checking %s states' % (s.depth, visited))
                break
