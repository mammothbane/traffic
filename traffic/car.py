import itertools


class Car:
    """A representation of an individual car in the traffic problem."""
    def __init__(self, parent, idx, direction, coord, length=2, player=False):
        self.player = player

        self._parent = parent
        self._idx = idx
        self._dir = direction.lower()
        self._coord = coord
        self._len = length

        assert self._dir == 'r' or self._dir == 'd'

    @property
    def index(self):
        return self._idx

    @property
    def x(self):
        return self._coord[0]

    @property
    def y(self):
        return self._coord[1]

    @property
    def forward(self):
        if self._dir == 'r':
            return self.x + 1, self.y
        else:
            return self.x, self.y + 1

    @property
    def back(self):
        if self._dir == 'r':
            return self.x - 1, self.y
        else:
            return self.x, self.y - 1

    def can_forward(self) -> bool:
        return self._can_move(True)

    def can_back(self) -> bool:
        return self._can_move(False)

    def _can_move(self, fwd):
        x, y = (0, 1)
        if self._dir == 'r':
            x, y = (1, 0)

        if not fwd:
            x *= -1
            y *= -1

        if not self.within_bounds(self._parent._dimens, (x, y)):
            return False

        for car in self._parent:
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

        if self._dir == 'r':
            for i in range(self._len):
                yield (x + i, y)
        else:
            for i in range(self._len):
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

    def __str__(self):
        return 'Car(idx=%s, dir=%s, coord=%s, len=%s, player=%s)' % (self._idx, self._dir, self._coord, self._len, self.player)

    def __repr__(self):
        return '%s%s %s%s' % ('player ' if self.player else '', self._coord, self._dir.upper(),
                              ' (len ' + str(self._len) + ')' if self._len != 2 else '')
