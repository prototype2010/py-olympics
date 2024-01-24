from entities import entity


class Team(entity.Entity):
    def __init__(self, event_row):
        self.team = event_row.team
        self.noc_name = event_row.noc

    def save(self):
        return
