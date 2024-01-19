from abc import *


class Entity:
    @abstractmethod
    def save(self):
        raise 'Should be overriden in child class'

