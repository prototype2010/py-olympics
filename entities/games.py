from entity import *


class Games(Entity):
    def __init__(self, event_row):
        self.year = event_row.year
        self.season = event_row.season
        self.city = event_row.city

    def save(self):
        return