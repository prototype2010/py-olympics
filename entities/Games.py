import Entity


class Games(Entity):
    def __init__(self, event_row):
        self.year = event_row['Year']
        self.season = event_row['Season']
        self.city = event_row['City']

    def save(self):
        return