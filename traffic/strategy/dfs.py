from itertools import count

from .strategy import Strategy
from ..state import State


class DFS(Strategy):
    """
    A basic DFS implementation.

    Not very smart or fast, but it does technically work, and avoids searching
    an infinite-depth tree by checking to see if we've seen a state before.

    Can handle the 4x4 example, but would take a very long time to exhaust all possible
    moves on any of the others.
    """

    def start(self, limit=None, p=True):
        queue = []

        cur = State(None, self._config.init_state, 0, self._config)

        for i in count():
            if i % 1000 == 0 and i > 0:
                if p:
                    print(i)
            if cur.complete():
                if p:
                    cur.report()
                    print('solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                return True, cur

            if cur.depth != limit:
                for car in cur:
                    if car.can_forward():
                        s = State(cur, {car.index: car.forward}, cur.depth + 1)
                        if not cur.seen(s):
                            queue.append(s)

                    if car.can_back():
                        s = State(cur, {car.index: car.back}, cur.depth + 1)
                        if not cur.seen(s):
                            queue.append(s)

            if len(queue) == 0:
                return False, None

            cur = queue.pop()
