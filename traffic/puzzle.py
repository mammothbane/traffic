from .car import Car


class Puzzle:
    """
    A representation of a state of the puzzle.

    Consists primarily of a list of cars.
    """
    def __init__(self, cfg, ser_state):
        self._config = cfg

        if ser_state:
            self._cars = [Car(self, k, v) for k, v in ser_state.items()]

    @property
    def config(self):
        return self._config

    @property
    def player(self):
        for x in self:
            if x.player:
                return x

    def __iter__(self):
        yield from self._cars

    def __getitem__(self, item):
        return self._cars[item]

    def __getattr__(self, item):
        return getattr(self._config, item)

    def serialize(self):
        return {car.index: (car.x, car.y) for car in self}

    def complete(self):
        """Check whether we've won."""
        return (self._exit, 0) in self.player.squares()

    def _car_in(self, coord):
        for car in self:
            if car.overlaps([coord]):
                return car.index
        return -1

    def print(self):
        out = ''
        for i in range(self.dimens[1]):
            for j in range(self.dimens[0]):
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
