from entities import entity


class Event(entity.Entity):
    def __init__(self, event_row):
        self.name = event_row.event

    def save(self):
        return