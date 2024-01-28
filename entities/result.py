from entities import entity


class Results(entity.Entity):
    def __init__(self, serialized_event, athlete, game, sport, event, team):
        super().__init__()

        self.medal = serialized_event.medal
        self.athlete = athlete
        self.game = game
        self.sport = sport
        self.event = event
        self.team = team

    def query_statement(self):
        return "INSERT INTO results (athlete_id, game_id, sport_id, event_id, medal) VALUES(?,?,?,?,?)"

    def parameters(self):
        return tuple([self.athlete.db_id(), self.game.db_id(), self.sport.db_id(), self.event.db_id(), self.medal])
