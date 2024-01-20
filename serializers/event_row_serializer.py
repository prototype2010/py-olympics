from enum import Enum


class Medal(Enum):
    Gold = 'Gold'
    Silver = 'Silver'
    Bronze = 'Bronze'


class EventRowSerializer:
    def __init__(self, event_row):
        self.id = self.parse_int(event_row['ID'])
        self.name = event_row['Name']
        self.name = event_row['Sex']
        self.name = self.parse_int(event_row['Age'])
        self.name = self.parse_int(event_row['Height'])
        self.name = self.parse_int(event_row['Weight'])
        self.name = event_row['Team']
        self.name = event_row['NOC']
        self.name = event_row['Games']
        self.name = self.parse_int(event_row['Year'])
        self.name = event_row['Season']
        self.name = event_row['City']
        self.name = event_row['Sport']
        self.name = event_row['Event']
        self.name = self.get_medal(event_row['Medal'])

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
