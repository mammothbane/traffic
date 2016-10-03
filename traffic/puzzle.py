from itertools import count

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

        assert players[0]._coord[0] == self._exit

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

    @property
    def player(self):
        for x in self:
            if x.player:
                return x

    def __iter__(self):
        yield from self._cars.values()

    def __getitem__(self, item):
        return self._cars[item]

    def _simple_cpy(self):
        return {car.index: car._coord for car in self}

    def with_car_fwd(self, i):
        cpy = self._simple_cpy()
        if self[i]._dir == 'r':
            cpy[i] = (cpy[i][0] + 1, cpy[i][1])
        else:
            cpy[i] = (cpy[i][0], cpy[i][1] + 1)
        return cpy

    def with_car_back(self, i):
        cpy = self._simple_cpy()
        if self[i]._dir == 'r':
            cpy[i] = (cpy[i][0] - 1, cpy[i][1])
        else:
            cpy[i] = (cpy[i][0], cpy[i][1] - 1)
        return cpy

    def use_cars(self, cars):
        for i, cp in cars.items():
            self[i]._coord = cp

    def items(self):
        yield from self._cars.items()

    def check(self):
        """Ensure all cars are within boundaries and non-overlapping."""
        for car in self:
            assert car.within_bounds(self._dimens)
            assert not any([car.overlaps(other) for other in self if other is not car])

    def complete(self) -> bool:
        return (self._exit, 0) in self.player.squares()

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
