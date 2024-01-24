from entities import entity


class Sport(entity.Entity):
    def __init__(self, event_row):
        self.name = event_row.sport

    def save(self):
        return
