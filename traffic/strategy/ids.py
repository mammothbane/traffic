from itertools import count

from .dfs import DFS
from .strategy import Strategy


class IDS(Strategy):
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
