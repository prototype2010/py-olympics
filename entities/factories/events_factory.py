from entities.factories import entity_factory
from entities import event

events_factory = entity_factory.EntityFactory(
            event.Event,
            lambda event, register: filter(lambda entity: entity.name == event.event, register)
        )