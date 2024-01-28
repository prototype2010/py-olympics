from entities import entity


class Team(entity.Entity):
    def __init__(self, event_row):
        super().__init__()

        self.team = event_row.team
        self.noc_name = event_row.noc

    def query_statement(self):
        return "INSERT INTO teams (name, noc_name) VALUES(?,?)"

    def parameters(self):
        return tuple([self.team, self.noc_name])