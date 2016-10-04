from collections import deque
from itertools import count

from .strategy import Strategy
from ..state import State


class BFS(Strategy):
    """
    A basic implementation of breadth-first search.

    Not suitable for puzzles with search depths greater than ~8 moves.
    """
    def start(self):
        queue = deque()

        cur = State(None, self._puzzle.simple_cpy(), 0)
        skips = 0

        seen = {cur.hash()}

        for i in count():
            if i % 1000 == 0 and i > 0:
                print('%s nodes processed (depth %s, %s skipped, %s in queue)' % (i, cur.depth, skips, len(queue)))

            if self._puzzle.complete():
                cur.report(self._puzzle)

                print('optimal solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                break

            for car in self._puzzle:
                if car.can_forward():
                    s = State(cur, {car.index: car.forward}, cur.depth + 1)
                    if s.hash() in seen:
                        skips += 1
                    else:
                        queue.append(s)
                        seen.add(s.hash())

                if car.can_back():
                    s = State(cur, {car.index: car.back}, cur.depth + 1)
                    if s.hash() in seen:
                        skips += 1
                    else:
                        queue.append(s)
                        seen.add(s.hash())

            cur = queue.popleft()

            self._puzzle.use_cars(cur.total_deltas)
