import logging
import abc

from itertools import chain


class Engine(abc.ABC):
    """
    Abstract class that all engines must inherit
    """
    name = None

    def __init__(self, delay: int = 5000, settings: dict = dict):
        self.delay = delay
        self.settings = settings
        self.log = logging.getLogger('dnz.engine.{}'.format(__class__))

    @abc.abstractmethod
    def run(self, host: str):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Engine: {}>'.format(self.name)


def available_engines(cls: object = Engine):
    """
    List engines available for scanning
    """
    return list(
        chain.from_iterable(
            [list(chain.from_iterable([[x], available_engines(x)])) for x in cls.__subclasses__()]
        )
    )


def get_engine(name: str):
    engines = available_engines()
    for engine in engines:
        if engine.name == name:
            return engine
