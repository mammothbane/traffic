class State:
    def __init__(self, parent, children):
        self._parent = parent
        self._children = children

    def __iter__(self):
        yield from self._children

    @property
    def parent(self):
        return self._parent

class StateTree:
    def __init__(self):
        self._nodes = {}