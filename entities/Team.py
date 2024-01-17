import Entity


class Team(Entity):
    def __init__(self, event_row):
        self.team = event_row['Team']
        self.noc_name = event_row['NOC']

    def save(self):
        return
