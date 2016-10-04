from copy import copy


class State:
    def __init__(self, parent, delta, depth):
        self._delta = delta
        self._checkpoint = None
        self._parent = parent
        self.depth = depth

        if parent:
            self._hashlist = parent._hashlist.union({self.hash()})
        else:
            self._hashlist = {self.hash()}

    @property
    def total_deltas(self):
        # if self._checkpoint:
        #     return copy(self._checkpoint)

        if not self._parent:
            return copy(self._delta)

        out = self._parent.total_deltas

        for k, v in self._delta.items():
            out[k] = v

        # only store full history every few levels
        # if self.depth % 5 == 0:
        #     self._checkpoint = copy(out)

        return out

    def seen(self, rep):
        if type(rep) is State:
            return rep.hash() in self._hashlist
        return rep in self._hashlist

    def hash(self):
        return ''.join(['%s%s%s' % (k, v[0], v[1]) for k, v in sorted(self.total_deltas.items())])

    def report(self, puzzle):
        if self._parent:
            self._parent.report(puzzle)

        puzzle.use_cars(self.total_deltas)
        puzzle.print()
        if self._parent and len(self._delta) == 1:
            k = list(self._delta.keys())[0]
            print('%s: %s -> %s' % (k, self._parent.total_deltas[k], self._delta[k]))
        else:
            print(self._delta)
        print()
