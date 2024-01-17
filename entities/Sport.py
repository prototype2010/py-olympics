import Entity


class Sport(Entity):
    def __init__(self, event_row):
        self.name = event_row['Sport']

    def save(self):
        return
