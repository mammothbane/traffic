from itertools import count

from .dfs import DFS


class IDS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self):
        for i in count():
            self._puzzle.print()
            dfs = DFS(self._puzzle)

            print('depth %s' % i)
            ok, s = dfs.start(i)
            if ok:
                print('solution found at depth %s' % s.depth)
                break
