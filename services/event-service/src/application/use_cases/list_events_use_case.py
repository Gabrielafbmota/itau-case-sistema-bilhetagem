from typing import List
from src.domain.entities.event_entity import Event
from src.domain.interfaces.event_repository_interface import EventRepositoryInterface


class ListEventsUseCase:
    def __init__(self, repository: EventRepositoryInterface):
        self.repository = repository

    def execute(self) -> List[Event]:
        return self.repository.list_all()
