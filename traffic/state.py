from copy import copy

from .car import Car


class State:
    def __init__(self, parent, delta, depth, config=None):
        self._delta = delta
        self._checkpoint = None
        self._parent = parent
        self.depth = depth

        assert parent or config

        self._config = config
        if not config:
            self._config = parent.config

        if parent:
            self._hashlist = parent._hashlist.union({self.hash()})
        else:
            self._hashlist = {self.hash()}

        self.__cars = None

    @property
    def _cars(self):
        if not self.__cars:
            self.__cars = [Car(self, k, v) for k, v in self.total_deltas.items()]
        return self.__cars

    def __iter__(self):
        yield from self._cars

    def __getitem__(self, item):
        return self._cars[item]

    def __getattr__(self, item):
        return getattr(self._config, item)

    def __lt__(self, other):
        return False

    def complete(self):
        """Check whether we've won."""
        return (self._exit, 0) in self.player.squares()

    @property
    def player(self):
        for x in self:
            if x.player:
                return x

    def print(self):
        out = ''
        for i in range(self.dimens[1]):
            for j in range(self.dimens[0]):
                car = self.car_in((j, i))
                if not car:
                    out += '. '
                    continue

                if car.player:
                    out += 'p '
                else:
                    out += str(car.index) + ' '
            out += '\n'

        print(out)

    @property
    def config(self):
        return self._config

    @property
    def total_deltas(self):
        """Compute the board state at this node."""
        if self._checkpoint:
            return copy(self._checkpoint)

        if not self._parent:
            return copy(self._delta)

        out = self._parent.total_deltas

        for k, v in self._delta.items():
            out[k] = v

        # only store full history every few levels
        if self.depth % 5 == 0:
            self._checkpoint = copy(out)

        return out

    def seen(self, rep):
        """Check whether any ancestor of this state represents the same board configuration."""
        if type(rep) is State:
            return rep.hash() in self._hashlist
        return rep in self._hashlist

    def hash(self):
        """Produce a unique hash representing the board state at this node."""
        return ''.join(['%s%s%s' % (k, v[0], v[1]) for k, v in sorted(self.total_deltas.items())])

    def report(self):
        """Print the list of moves required to reach this state."""
        if self._parent:
            self._parent.report()

        self.print()

        if self._parent and len(self._delta) == 1:
            k = list(self._delta.keys())[0]
            print('%s: %s -> %s' % (k, self._parent.total_deltas[k], self._delta[k]))
        else:
            print(self._delta)
        print()

    def car_in(self, coord):
        for car in self:
            if car.overlaps([coord]):
                return car
