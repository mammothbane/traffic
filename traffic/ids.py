from itertools import count

from .dfs import DFS


class IDS:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._dfs = DFS(puzzle)

    def start(self):
        for i in count():
            if self._dfs.start(i):
                break
