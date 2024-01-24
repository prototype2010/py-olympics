import csv
from serializers.event_row_serializer import EventRowSerializer
from entities.factories import sports_factory,results_factory,games_factory, events_factory, athletes_factory, teams_factory
from entities import event,sport,athlete, games, result, team

FILE_NAME = 'athlete_events.csv'


def parse():
    with open(FILE_NAME, 'r') as file:
        rows = csv.reader(file)
        all_rows = list(rows)
        headers = all_rows[0]
        values = all_rows[1:]

        headers_to_values = map(lambda row: dict(zip(headers, row)), values)
        serialized_events = list(map(lambda row: EventRowSerializer(row), headers_to_values))

        for serialized_event in serialized_events:

            athlete = athletes_factory.athletes_factory.create(serialized_event)
            sport = sports_factory.sports_factory.create(serialized_event)
            team = teams_factory.teams_factory.create(serialized_event)
            game = games_factory.games_factory.create(serialized_event)
            event = events_factory.events_factory.create(serialized_event)

            result = results_factory.results_factory.create(
                serialized_event,
                athlete=athlete,
                sport=sport,
                team=team,
                game=game,
                event=event
            )

            a=1
            # def mapper(event):
            #     return sportsman_factory.create(event)

        athletes_factory.athletes_factory
        # sportsmen = list(map(mapper, serialized_events))
        # sportsmen = map(lambda event: sportsman_factory.create(event), serialized_events)









