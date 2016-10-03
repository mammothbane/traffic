from .dfs import DFS


class IDS:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._dfs = DFS(puzzle)

    def start(self):
        i = 1

        while True:
            print('trying up to depth %s' % i)
            if self._dfs.start(i):
                break

            i *= 2
