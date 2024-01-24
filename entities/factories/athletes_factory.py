from entities.factories import entity_factory
from entities import athlete

athletes_factory = entity_factory.EntityFactory(
            athlete.Athlete,
            lambda event, register: filter(lambda entity: entity.id == event.id, register)
        )