from enum import Enum


class Medal(Enum):
    Gold = 'Gold'
    Silver = 'Silver'
    Bronze = 'Bronze'


class EventRowSerializer:
    def __init__(self, event_row):
        self.id = self.parse_int(event_row['ID'])
        self.name = event_row['Name']
        self.sex = event_row['Sex']
        self.age = self.parse_int(event_row['Age'])
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
        self.medal = self.get_medal(event_row['Medal'])

    @staticmethod
    def get_medal(medal_value):
        if medal_value in Medal._member_names_:
            return medal_value
        else:
            return None

    @staticmethod
    def parse_int(int_value):
        try:
            return int(int_value)
        except ValueError:
            return None
