from abc import *

class Strategy(metaclass=ABC):
    def __init__(self, constructor, lookup_callback):
        self.constructor = constructor
        self.lookup_callback = lookup_callback

    @abstractmethod
    def should_create_new(self, register):
        raise 'Should be overriden in child class'

    @abstractmethod
    def create(self, event_row, register):
        raise 'Should be overriden in child class'
