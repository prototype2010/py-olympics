from entities import entity
from datetime import datetime
import json


class Athlete(entity.Entity):
    def __init__(self, event_row, team):
        super().__init__()

        self.id = event_row.id
        self.name = event_row.name
        self.sex = event_row.sex
        self.age = event_row.age
        self.height = event_row.height
        self.weight = event_row.weight
        self.team = team

    def query_statement(self):
        return "INSERT INTO athletes (id,full_name,year_of_birth,sex,params,team_id) VALUES(?,?,?,?,?,?)"

    def parameters(self):
        year_of_birth = datetime.now().year - self.age
        params = json.dumps({'height': self.height, 'weight': self.weight})

        team_id = self.team.db_id()

        return tuple([self.id, self.name, year_of_birth, self.sex, params, team_id ])

