from src.domain.entities.ticket_entity import Ticket
from src.domain.interfaces.ticket_repository import TicketRepositoryInterface


class CreateTicketUseCase:
    def __init__(self, ticket_repository: TicketRepositoryInterface):
        self.ticket_repository = ticket_repository

    def execute(self, ticket: Ticket) -> Ticket:
        return self.ticket_repository.create(ticket)
