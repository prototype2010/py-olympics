from entities import entity


class Athlete(entity.Entity):
    def __init__(self, event_row):
        self.id = event_row.id
        self.name = event_row.name
        self.sex = event_row.sex
        self.age = event_row.age
        self.height = event_row.height
        self.weight = event_row.weight

    def save(self):
        return