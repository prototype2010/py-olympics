

class EntityFactory:
    def __init__(self, constructor, lookup_callback=None):
        self.register = list()
        self.constructor = constructor
        self.lookup_callback = lookup_callback

    def _find_existing(self, event):
        if not self.lookup_callback:
            return None

        return next(self.lookup_callback(event, self.register), None)

    def _create_new(self, serialized_event, **kwargs):
        entity = self.constructor(serialized_event, **kwargs)

        self.register.append(entity)

        return entity

    def create(self, serialized_event, **kwargs):
        existing_entity = self._find_existing(serialized_event)

        if existing_entity:
            return existing_entity
        else:
            return self._create_new(serialized_event, **kwargs)

