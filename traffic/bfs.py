from collections import deque
from itertools import count

from .state import State


class BFS:
    """
    A basic implementation of breadth-first search.

    Not suitable for puzzles with search depths greater than ~8 moves.
    """
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self):
        queue = deque()

        cur = State(None, self._puzzle.simple_cpy(), 0)
        skips = 0

        for i in count():
            if i % 1000 == 0 and i > 0:
                print('%s nodes processed (depth %s, %s skipped, %s in queue)' % (i, cur.depth, skips, len(queue)))

            if self._puzzle.complete():
                cur.report(self._puzzle)

                print('optimal solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                break

            for car in self._puzzle:
                if car.can_forward():
                    s = State(cur, self._puzzle.with_car_fwd(car.index), cur.depth + 1)
                    if cur.seen(s):
                        skips += 1
                    else:
                        queue.append(s)

                if car.can_back():
                    s = State(cur, self._puzzle.with_car_back(car.index), cur.depth + 1)
                    if cur.seen(s):
                        skips += 1
                    else:
                        queue.append(s)

            cur = queue.popleft()

            self._puzzle.use_cars(cur.total_deltas)
