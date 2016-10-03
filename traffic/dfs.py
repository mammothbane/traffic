from itertools import count


class DFS:
    def __init__(self, puzzle):
        self._puzzle = puzzle

    def start(self, limit=0):
        queue = []

        seen = set()

        for i in count():
            if i % 1000 == 0 and i > 0:
                print(i)
            if self._puzzle.complete():
                self._puzzle.print()
                print('completed in %s steps\n' % i)
                return True

            for car in self._puzzle:
                if car.can_forward():
                    queue.append(self._puzzle.with_car_fwd(car.index))
                if car.can_back():
                    queue.append(self._puzzle.with_car_back(car.index))

            cars = queue.pop()
            hs = self.hash_cars(cars)

            while hs in seen:
                cars = queue.pop()
                hs = self.hash_cars(cars)

            seen.add(hs)

            self._puzzle.use_cars(cars)

        return False

    @staticmethod
    def hash_cars(elem):
        items = ['%s%s%s' % (k, v[0], v[1]) for k, v in elem.items()]
        items.sort()
        return ''.join(items)
