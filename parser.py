import csv
from serializers.event_row_serializer import EventRowSerializer
from entities.factories import entity_factory
from entities import entity,event,sport,sportsman

FILE_NAME = 'athlete_events.csv'


def parse():
    with open(FILE_NAME, 'r') as file:
        rows = csv.reader(file)
        all_rows = list(rows)
        headers = all_rows[0]
        values = all_rows[1:]

        headers_to_values = map(lambda row: dict(zip(headers, row)), values)
        serialized_events = map(lambda row: EventRowSerializer(row), headers_to_values)


        sportsman_factory = entity_factory.EntityFactory(
            sportsman,
            lambda event,register: filter(lambda entity: entity.id == event.id, register)
        )



        sportsmen = map(lambda event: sportsman_factory.create(event), serialized_events)


        print(sportsman_factory.register)








