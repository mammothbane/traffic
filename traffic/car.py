import itertools


class Car:
    """A representation of an individual car in the traffic problem."""
    def __init__(self, parent, idx, dir, coord, length=2, player=False):
        self.player = player

        self._parent = parent
        self._idx = idx
        self._dir = dir.lower()
        self._coord = coord
        self._len = length

        assert self._dir == 'r' or self._dir == 'd'

    def forward(self) -> bool:
        """Move the car forward, returning true if the action was successful."""
        if not self.can_forward():
            return False

        if self._dir == 'r':
            self._coord[0] += 1
        else:
            self._coord[1] += 1

        return True

    def back(self) -> bool:
        """Move the car backward, returning true if the action was successful."""
        if not self.can_back():
            return False

        if self._dir == 'r':
            self._coord[0] -= 1
        else:
            self._coord[1] -= 1

        return True

    def can_forward(self) -> bool:
        return self._can_move(True)

    def can_back(self) -> bool:
        return self._can_move(False)

    def _can_move(self, fwd):
        offset = [0, 1]
        if dir == 'r':
            offset = [1, 0]

        if not fwd:
            offset[0] *= -1
            offset[1] *= -1

        offset = tuple(offset)

        if not self.within_bounds(self._parent._dimens, offset):
            return False

        if any([car.overlaps(self.squares(offset)) for car in self._parent]):
            return False

        return True

    def overlaps(self, other) -> bool:
        """
        Check whether this car overlaps any of the squares in other.

        :arg other: an iterable of (x, y) coordinate tuples
        """
        itr = other
        if type(other) is Car:
            itr = other.squares

        for sq1, sq2 in itertools.product(self.squares, itr):
            if sq1 == sq2:
                return True

        return False

    def squares(self, offset=(0, 0)):
        """Generate squares within the bounds of the car."""
        x, y = (self._coord[0] + offset[0], self._coord[1] + offset[1])

        if self._dir == 'r':
            for i in range(self._len):
                yield (x + i, y)
        else:
            for i in range(self._len):
                yield (x, y + i)

    def within_bounds(self, bounds, offset=(0, 0)) -> bool:
        adjusted = (self._coord[0] + offset[0], self._coord[1] + offset[1])

        if self._dir == 'r':
            if not bounds[1] > adjusted[1] >= 0:
                return False
            if not bounds[0] > adjusted[0] + self._len and adjusted[0] >= 0:
                return False
        else:
            if not bounds[0] > adjusted[0] >= 0:
                return False
            if not bounds[1] > adjusted[1] + self._len and adjusted[1] >= 0:
                return False

        return True

    @property
    def dimens(self):
        """Get the bounds of the car as two pairs of coordinates."""
        (x, y) = self._coord
        if self._dir == 'r':
            return (x, y), (x + self._len, y)

        return (x, y), (x, y + self._len)

    def __str__(self):
        return 'Car(idx=%s, dir=%s, coord=%s, len=%s, player=%s)' % (self._idx, self._dir, self._coord, self._len, self.player)

    def __repr__(self):
        return '%s%s %s%s' % ('player ' if self.player else '', self._coord, self._dir.upper(),
                              ' (len ' + str(self._len) + ')' if self._len != 2 else '')
