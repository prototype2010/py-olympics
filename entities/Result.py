import  Entity


class Results(Entity):
    def __init__(self, event_row, athlete, game, sport, event):
        self.id = event_row['Medal']
        self.athlete = athlete
        self.game = game
        self.sport = sport
        self.event = event

    def save(self):
        return
