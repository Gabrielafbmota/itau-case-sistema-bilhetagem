from src.domain.interfaces.ticket_repository import TicketRepositoryInterface


class DeleteTicketUseCase:
    def __init__(self, ticket_repository: TicketRepositoryInterface):
        self.ticket_repository = ticket_repository

    def execute(self, ticket_id: int) -> None:
        self.ticket_repository.delete(ticket_id)
