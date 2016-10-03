class Traffic:
    """
    A representation of the whole state of the problem.

    Consists primarily of a list of cars.
    """
    def __init__(self, goal, cars, dimens=(6, 6)):
        players = [x for x in cars if x.player]
        assert len(players) == 1

        self.player = players[0]
        self._dimens = dimens
        self._cars = cars
        self._exit = goal

        for idx, car in self.items():
            car._parent = self
            car._idx = idx

        self.check()

    def __iter__(self):
        yield from self._cars

    def __getitem__(self, item):
        return self._cars[item]

    def items(self):
        return zip(range(0), self)

    def check(self):
        for car in self:
            try:
                assert car.within_bounds(self._dimens)
            except AssertionError:
                print(car)
                raise

    def complete(self) -> bool:
        return (0, self._exit) in self.player.squares()

    def _car_in(self, coord):
        for i, car in self.items():
            if car.overlaps([coord]):
                return i

    def print(self) -> str:
        out = ''
        for i in range(0, self._dimens[1]):
            for j in range(0, self._dimens[0]):
                car = self._car_in((j, i))
                if car:
                    out += str(car._idx)
                else:
                    out += 'x'
            out += '\n'

        print(out)
