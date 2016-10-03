from itertools import count, product

from .car import Car


class Puzzle:
    """
    A representation of the whole state of the problem.

    Consists primarily of a list of cars.
    """
    def __init__(self, file_name=None, goal=None, cars=None, dimens=(6, 6)):
        if file_name:
            self._load_from_file(file_name)
        else:
            self._dimens = dimens
            self._cars = cars
            self._exit = goal

            for idx, car in self.items():
                car._parent = self
                car._idx = idx

        players = [x for x in self if x.player]
        assert len(players) == 1
        self.player = players[0]

        self.check()

    def _load_from_file(self, file_name):
        import json
        with open(file_name) as f:
            data = json.load(f)

        self._cars = {}

        for i, elem in zip(count(), data['cars']):
            self._cars[i] = Car(self,
                                i,
                                elem['dir'],
                                (elem['x'], elem['y']),
                                elem.get('len', 2),
                                elem.get('player', False))

        self._dimens = (data['dimens']['x'], data['dimens']['y'])
        self._exit = data['exit']

    def __iter__(self):
        yield from self._cars.values()

    def __getitem__(self, item):
        return self._cars[item]

    def to_list(self):
        return [self._car_in((i, j)) for i, j in product(range(self._dimens[0]), range(self._dimens[1]))]

    def items(self):
        yield from self._cars.items()

    def check(self):
        """Ensure all cars are within boundaries and non-overlapping."""
        for car in self:
            assert car.within_bounds(self._dimens)
            assert not any([car.overlaps(other) for other in self if other is not car])

    def complete(self) -> bool:
        return (0, self._exit) in self.player.squares()

    def _car_in(self, coord):
        for i, car in self.items():
            if car.overlaps([coord]):
                return i
        return -1

    def print(self) -> str:
        out = ''
        for i in range(self._dimens[1]):
            for j in range(self._dimens[0]):
                car_idx = self._car_in((j, i))
                if car_idx == -1:
                    out += '. '
                    continue

                if self[car_idx].player:
                    out += 'p '
                else:
                    out += str(car_idx) + ' '
            out += '\n'

        print(out)
