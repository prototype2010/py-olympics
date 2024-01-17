from abc import ABC


class EntityFactory(metaclass=ABC):
    register = list()

    def __init__(self, strategy, constructor, pick_keys_list, lookup_keys_list):
        self.constructor = constructor
        self.strategy = strategy
        self.pick_keys_list = pick_keys_list
        self.lookup_keys_list = lookup_keys_list

    def create(self, event_row):

        if self.strategy.should_create_new(self.register):
            entity = self.constructor()

        entity = self.strategy.create(event_row, self.register)
        self.register.append(entity)

        return entity
