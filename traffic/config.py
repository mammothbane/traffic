import json

from .carconfig import CarConfig


class Config:
    """Basic configuration of the problem."""
    def __init__(self, file):
        with open(file) as f:
            data = json.load(f)

        self._cars = []
        self._dimens = (data['dimens']['x'], data['dimens']['y'])
        self._exit = data['exit']

        for i, elem in enumerate(data['cars']):
            self._cars.append(CarConfig(self, elem['dir'], i, (elem['x'], elem['y']),
                                        elem.get('len', 2), elem.get('player', False)))

        players = [x for x in self if x.player]
        assert len(players) == 1
        assert players[0].default_x == self._exit

    def __iter__(self):
        yield from self._cars

    def __getitem__(self, i):
        return self._cars[i]

    @property
    def init_state(self):
        return {elem.index: (elem.default_x, elem.default_y) for elem in self}

    @property
    def dimens(self):
        return self._dimens

    @property
    def exit(self):
        return self._exit
