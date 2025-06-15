from typing import Optional
from src.domain.entities.ticket_entity import Ticket
from src.domain.interfaces.ticket_repository import TicketRepositoryInterface


class GetTicketUseCase:
    def __init__(self, ticket_repository: TicketRepositoryInterface):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_id: int) -> Optional[Ticket]:
        return self.ticket_repository.get_by_id(ticket_id)
