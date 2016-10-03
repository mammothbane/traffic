from collections import deque
from itertools import count

from .state import State


class BFS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self):
        queue = deque()

        cur = State(None, {}, 0)
        seen = {cur.hash()}

        for i in count():
            if i % 1000 == 0 and i > 0:
                print(i)
            if self._puzzle.complete():
                cur.report(self._puzzle)

                print('solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                break

            for car in self._puzzle:
                if car.can_forward():
                    s = State(cur, self._puzzle.with_car_fwd(car.index), cur.depth + 1)
                    hs = s.hash()

                    if hs not in seen:
                        queue.append(s)
                        seen.add(hs)

                if car.can_back():
                    s = State(cur, self._puzzle.with_car_back(car.index), cur.depth + 1)
                    hs = s.hash()

                    if hs not in seen:
                        queue.append(s)
                        seen.add(hs)

            cur = queue.popleft()

            self._puzzle.use_cars(cur.total_deltas)

