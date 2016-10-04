import itertools


class Car:
    """A representation of an individual car in the traffic problem."""
    def __init__(self, state, index, coord=None):
        self._state = state
        self._index = index

        if coord:
            self._coord = coord
        else:
            self._coord = self.default_coords

    def __len__(self):
        return len(self.car_config)

    def __getattr__(self, item):
        return getattr(self.car_config, item)

    @property
    def car_config(self):
        return self._state.config[self._index]

    @property
    def x(self):
        return self._coord[0]

    @property
    def y(self):
        return self._coord[1]

    @property
    def forward(self):
        if self.dir == 'r':
            return self.x + 1, self.y
        else:
            return self.x, self.y + 1

    @property
    def back(self):
        if self.dir == 'r':
            return self.x - 1, self.y
        else:
            return self.x, self.y - 1

    def can_forward(self) -> bool:
        return self._can_move(True)

    def can_back(self) -> bool:
        return self._can_move(False)

    def _can_move(self, fwd):
        x, y = (0, 1)
        if self.dir == 'r':
            x, y = (1, 0)

        if not fwd:
            x *= -1
            y *= -1

        if not self.within_bounds(self._state.dimens, (x, y)):
            return False

        for car in self._state:
            if car is self:
                continue
            if car.overlaps(self.squares((x, y))):
                return False

        return True

    def overlaps(self, other) -> bool:
        """
        Check whether this car overlaps any of the squares in other.

        :arg other: an iterable of (x, y) coordinate tuples, or a Car
        """
        itr = other
        if type(other) is Car:
            itr = other.squares()

        for sq1, sq2 in itertools.product(self.squares(), itr):
            if sq1 == sq2:
                return True

        return False

    def squares(self, offset=(0, 0)):
        """Generate all squares within the bounds of the car."""
        x, y = (self._coord[0] + offset[0], self._coord[1] + offset[1])

        if self.dir == 'r':
            for i in range(len(self)):
                yield (x + i, y)
        else:
            for i in range(len(self)):
                yield (x, y + i)

    def within_bounds(self, bounds, offset=(0, 0)) -> bool:
        b_x = bounds[0]
        b_y = bounds[1]

        for sq in self.squares(offset):
            if not b_x > sq[0] >= 0:
                return False
            if not b_y > sq[1] >= 0:
                return False

        return True

    @property
    def blocked_by(self):
        if self.can_forward() or self.can_back():
            return

        fwd = self._state.car_in(self.forward)
        bck = self._state.car_in(self.back)

        return [x for x in [fwd, bck] if x]

    def __str__(self):
        return 'Car(idx=%s, dir=%s, coord=%s, len=%s, player=%s)' % (self.index, self.dir, self._coord, len(self), self.player)

    def __repr__(self):
        return '%s%s %s%s' % ('player ' if self.player else '', self._coord, self.dir.upper(),
                              ' (len ' + str(len(self)) + ')' if len(self) != 2 else '')
