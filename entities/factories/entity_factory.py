

class EntityFactory:
    register = list()

    def __init__(self, constructor, lookup_callback=None):
        self.constructor = constructor
        self.lookup_callback = lookup_callback

    def _find_existing(self, event):
        if not self.lookup_callback:
            return None

        return next(self.lookup_callback(event, self.register), None)

    def _create_new(self, event):
        entity = self.constructor(event)
        self.register.append(entity)

        return entity

    def create(self, event):
        print('call')
        existing_entity = self._find_existing(event)

        if existing_entity:
            return existing_entity
        else:
            return self._create_new(event)

