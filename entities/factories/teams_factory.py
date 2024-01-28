from entities.factories import entity_factory
from entities import team

teams_factory = entity_factory.EntityFactory(
            team.Team,
            lambda event, register: filter(lambda entity: entity.noc_name == event.noc, register)
        )