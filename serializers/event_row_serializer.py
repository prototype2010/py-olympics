
class EventRowSerializer:
    def __init__(self, event_row):
        self.id = self.parse_int(event_row['ID'])
        self.name = event_row['Name']
        self.sex = event_row['Sex']
        self.age = self.parse_int(event_row['Age'], 0)
        self.height = self.parse_int(event_row['Height'])
        self.weight = self.parse_int(event_row['Weight'])
        self.team = event_row['Team']
        self.noc = event_row['NOC']
        self.games = event_row['Games']
        self.year = self.parse_int(event_row['Year'])
        self.season = event_row['Season']
        self.city = event_row['City']
        self.sport = event_row['Sport']
        self.event = event_row['Event']
        self.medal = self.get_medal_value(event_row['Medal'])

    @staticmethod
    def get_medal_value(medal_value):
        if medal_value == 'Gold':
            return 1
        elif medal_value == 'Silver':
            return 2
        elif medal_value == 'Bronze':
            return 3
        else:
            return 0

    @staticmethod
    def parse_int(int_value, fallback_value=None):
        try:
            return int(int_value)
        except ValueError:
            return fallback_value
