from typing import List
from src.domain.entities.ticket_entity import Ticket
from src.domain.interfaces.ticket_repository import TicketRepositoryInterface


class ListTicketsByEventUseCase:
    def __init__(self, ticket_repository: TicketRepositoryInterface):
        self.ticket_repository = ticket_repository

    def execute(self, event_id: int) -> List[Ticket]:
        return self.ticket_repository.list_by_event(event_id)
