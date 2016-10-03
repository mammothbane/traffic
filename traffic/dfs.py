from itertools import count

from .state import State


class DFS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self, limit=None, p=True):
        queue = []

        cur = State(None, self._puzzle._simple_cpy(), 0)
        seen = {cur.hash()}

        for i in count():
            if i % 1000 == 0 and i > 0:
                if p:
                    print(i)
            if self._puzzle.complete():
                if p:
                    cur.report(self._puzzle)
                    print('solution found at depth %s. completed in %s steps\n' % (cur.depth, i))
                return True, cur

            if cur.depth != limit:
                for car in self._puzzle:
                    if car.can_forward():
                        s = State(cur, {car.index: car.forward}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen:
                            queue.append(s)
                            seen.add(hs)

                    if car.can_back():
                        s = State(cur, {car.index: car.back}, cur.depth + 1)
                        hs = s.hash()

                        if hs not in seen:
                            queue.append(s)
                            seen.add(hs)

            if len(queue) == 0:
                return False, None

            cur = queue.pop()
            self._puzzle.use_cars(cur.total_deltas)
