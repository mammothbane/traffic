from itertools import count

from .strategy import Strategy
from ..state import State


class DFS(Strategy):
    """A basic DFS implementation."""

    def start(self, limit=None, p=True):
        queue = []

        cur = State(None, self._config.init_state, 0, self._config)
        seen = {cur.hash(): 0}

        for i in count():
            if i % 1000 == 0 and i > 0:
                if p:
                    print(i)
            if cur.complete():
                if p:
                    cur.report()
                    print('solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                return True, cur, i

            if cur.depth != limit:
                for car in cur:
                    if car.can_forward():
                        s = State(cur, {car.index: car.forward}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen or cur.depth < seen[hs]:
                            queue.append(s)
                            seen[hs] = cur.depth

                    if car.can_back():
                        s = State(cur, {car.index: car.back}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen or cur.depth < seen[hs]:
                            seen[hs] = cur.depth
                            queue.append(s)

            if len(queue) == 0:
                return False, None, i

            cur = queue.pop()
