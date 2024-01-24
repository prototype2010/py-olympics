from entities import entity


class Results(entity.Entity):
    def __init__(self, serialized_event, athlete, game, sport, event, team):

        self.medal = serialized_event.medal
        self.athlete = athlete
        self.game = game
        self.sport = sport
        self.event = event
        self.team = team

    def save(self):
        return
