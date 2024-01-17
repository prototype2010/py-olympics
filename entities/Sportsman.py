import Entity

class Sportsman(Entity):
    def __init__(self, event_row):
        self.name = event_row['Name']
        self.sex = event_row['Sex']
        self.age = event_row['Age']
        self.height = event_row['Height']
        self.weight = event_row['Weight']

    def save(self):
        return