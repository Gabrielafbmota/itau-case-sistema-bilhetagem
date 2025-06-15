from typing import Optional
from src.domain.entities.event_entity import Event
from src.domain.interfaces.event_repository_interface import EventRepositoryInterface


class UpdateEventUseCase:
    def __init__(self, repository: EventRepositoryInterface):
        self.repository = repository

    def execute(self, event_id: int, event: Event) -> Optional[Event]:
        return self.repository.update(event_id, event)
