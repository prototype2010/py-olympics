from abc import *
from database.Connection import Connection


class Entity:
    def __init__(self):
        self.saved = False
        self._db_id = None

    def save(self):
        if self.saved:
            return self
        else:
            entity = Connection().execute_query(self.query_statement(), self.parameters())
            self.saved = True
            self._db_id = entity['id']

            return self

    def db_id(self):
        return self.save()._db_id

    @abstractmethod
    def query_statement(self):
        raise 'Should be overriden in child class'

    @abstractmethod
    def parameters(self):
        raise 'Should be overriden in child class'
