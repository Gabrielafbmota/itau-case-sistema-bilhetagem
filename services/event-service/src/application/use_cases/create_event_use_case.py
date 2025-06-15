from src.domain.entities.event_entity import Event
from src.domain.interfaces.event_repository_interface import EventRepositoryInterface


class CreateEventUseCase:
    def __init__(self, repository: EventRepositoryInterface):
        self.repository = repository

    def execute(self, event: Event) -> Event:
        return self.repository.create(event)
