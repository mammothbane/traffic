from collections import deque
from itertools import count


class BFS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self):
        queue = deque()

        for i in count():
            self._puzzle.print()
            if i % 1000 == 0:
                print(i)
            if self._puzzle.complete():
                self._puzzle.print()
                break

            for car in self._puzzle:
                if car.can_forward():
                    queue.append(self._puzzle.with_car_fwd(car.index))
                if car.can_back():
                    queue.append(self._puzzle.with_car_back(car.index))

            cars = queue.popleft()
            self._puzzle.use_cars(cars)