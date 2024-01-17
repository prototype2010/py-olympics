from abc import *


class Entity(metaclass=ABC):
    @abstractmethod
    def save(self):
        raise 'Should be overriden in child class'

