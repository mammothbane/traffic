from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    def __init__(self, config):
        self._config = config

    @abstractmethod
    def start(self):
        pass
