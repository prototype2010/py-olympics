from entities.factories import entity_factory
from entities import team

teams_factory = entity_factory.EntityFactory(
            team.Team,
            lambda event, register: filter(lambda entity: entity.team == event.team
                                                          and entity.noc_name == event.noc, register)
        )