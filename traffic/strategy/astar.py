from itertools import count
from queue import PriorityQueue

from .strategy import Strategy
from ..state import State


class AStar(Strategy):
    def __init__(self, config, heuristic):
        super().__init__(config)
        self._h = heuristic

    def start(self, limit=None):
        queue = PriorityQueue()

        cur = State(None, self._config.init_state, 0, self._config)
        seen = {cur.hash(): 0}

        for i in count():
            if i % 1000 == 0 and i > 0:
                print(i)
            if cur.complete():
                cur.report()
                print('optimal solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                return True, cur

            if cur.depth != limit:
                for car in cur:
                    if car.can_forward():
                        s = State(cur, {car.index: car.forward}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen or cur.depth < seen[hs]:
                            queue.put((s.depth + self._h.estimate(s), s))
                            seen[hs] = cur.depth

                    if car.can_back():
                        s = State(cur, {car.index: car.back}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen or cur.depth < seen[hs]:
                            queue.put((s.depth + self._h.estimate(s), s))
                            seen[hs] = cur.depth

            if queue.empty():
                return False, None

            prio, nxt = queue.get()
            cur = nxt
