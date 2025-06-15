from typing import Optional
from src.domain.entities.ticket_entity import Ticket
from src.domain.interfaces.ticket_repository import TicketRepositoryInterface


class UpdateTicketUseCase:
    def __init__(self, ticket_repository: TicketRepositoryInterface):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_id: int, ticket: Ticket) -> Optional[Ticket]:
        return self.ticket_repository.update(ticket_id, ticket)
