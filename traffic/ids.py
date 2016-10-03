from .dfs import DFS


class IDS:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._dfs = DFS(puzzle)

    def start(self):
        i = 1

        while True:
            print('trying up to depth %s' % i)
            ok, s = self._dfs.start(i, p=False)
            if ok:
                print('solution found at %s' % s.depth)
                self.bsearch(i // 2, s.depth, s)
                break

            i *= 2

    def bsearch(self, lower, upper, cur):
        print('bsearch: %s | %s' % (lower, upper))
        if lower == upper:
            print('optimal solution at depth %s' % lower)
            if cur:
                cur.report(self._puzzle)
            return

        target = (lower + upper) // 2
        ok, nc = self._dfs.start(target, p=False)
        if ok:
            self.bsearch(lower, target, nc)
        else:
            self.bsearch(target, upper, nc)
