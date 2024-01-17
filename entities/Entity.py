
class Entity(metaclass=ABC):
    @abc.abstractmethod
    def save(self):
        raise 'Should be overriden in child class'

