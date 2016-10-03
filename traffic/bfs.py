from collections import deque

class BFS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self):
        queue = deque()

        for car in self._puzzle:
            if car.can_forward():
                queue.append(car)