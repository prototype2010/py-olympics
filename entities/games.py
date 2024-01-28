from entities import entity


class Games(entity.Entity):
    def __init__(self, event_row):
        super().__init__()

        self.year = event_row.year
        self.season = event_row.season
        self.city = event_row.city

    def query_statement(self):
        return "INSERT INTO games (year, season, city) VALUES(?,?,?)"

    def parameters(self):
        return tuple([self.year, self.season, self.city,])