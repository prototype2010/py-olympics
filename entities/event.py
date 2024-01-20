from entities import entity


class Event(entity.Entity):
    def __init__(self, event_row):
        self.name = event_row['Event']

    def save(self):
        return