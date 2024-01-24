from entities.factories import entity_factory
from entities import sport

sports_factory = entity_factory.EntityFactory(
            sport.Sport,
            lambda event, register: filter(lambda entity: entity.name == event.sport, register)
        )
