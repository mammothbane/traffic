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

    @property
    def index(self):
        return self._idx

    def forward(self) -> bool:
        """Move the car forward, returning true if the action was successful."""
        if not self.can_forward():
            return False

        (x, y) = self._coord

        if self._dir == 'r':
            x += 1
        else:
            y += 1

        self._coord = (x, y)
        return True

    def back(self) -> bool:
        """Move the car backward, returning true if the action was successful."""
        if not self.can_back():
            return False

        (x, y) = self._coord

        if self._dir == 'r':
            x -= 1
        else:
            y -= 1

        self._coord = (x, y)
        return True

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

        :arg other: an iterable of (x, y) coordinate tuples
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
