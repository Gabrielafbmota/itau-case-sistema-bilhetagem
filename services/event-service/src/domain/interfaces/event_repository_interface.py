from typing import List, Optional
from src.domain.entities.event_entity import Event


class EventRepositoryInterface:
    def create(self, event: Event) -> Event:
        raise NotImplementedError

    def get_by_id(self, event_id: int) -> Optional[Event]:
        raise NotImplementedError

    def list_all(self) -> List[Event]:
        raise NotImplementedError

    def update(self, event_id: int, event: Event) -> Optional[Event]:
        raise NotImplementedError

    def delete(self, event_id: int) -> None:
        raise NotImplementedError
