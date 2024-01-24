from entities.factories import entity_factory
from entities import games


def find_existing_game(event, register):
    return filter(lambda entity: entity.year == event.year
                          and entity.season == event.season
                          and entity.city == event.city, register)


games_factory = entity_factory.EntityFactory(
    games.Games,
    lambda event, register: find_existing_game(event, register))
