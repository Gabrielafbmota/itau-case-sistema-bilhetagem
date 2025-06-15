from typing import List, Optional
from src.domain.entities.ticket_entity import Ticket


class TicketRepositoryInterface:
    def create(self, ticket: Ticket) -> Ticket:
        raise NotImplementedError

    def get_by_id(self, ticket_id: int) -> Optional[Ticket]:
        raise NotImplementedError

    def list_by_event(self, event_id: int) -> List[Ticket]:
        raise NotImplementedError

    def update(self, ticket_id: int, ticket: Ticket) -> Ticket:
        raise NotImplementedError

    def delete(self, ticket_id: int) -> None:
        raise NotImplementedError
