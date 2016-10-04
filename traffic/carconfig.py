class CarConfig:
    """Static information about an individual car."""

    def __init__(self, config, direction, index, default_coords, length=2, player=False):
        self._config = config
        self._dir = direction
        self._len = length
        self._player = player
        self._idx = index
        self._default = default_coords

        assert self._dir == 'r' or self._dir == 'd'

    @property
    def dir(self):
        return self._dir

    @property
    def player(self):
        return self._player

    @property
    def index(self):
        return self._idx

    @property
    def default_coords(self):
        return self._default

    @property
    def default_x(self):
        return self._default[0]

    @property
    def default_y(self):
        return self._default[1]

    def __len__(self):
        return self._len
