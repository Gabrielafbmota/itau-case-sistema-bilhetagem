from src.domain.interfaces.ticket_repository_interface import TicketRepositoryInterface


class IncrementTicketStockUseCase:
    def __init__(self, repository: TicketRepositoryInterface):
        self.repository = repository

    def execute(self, ticket_id: int, quantity: int) -> None:
        ticket = self.repository.get_by_id(ticket_id)
        if not ticket:
            raise ValueError("Ticket não encontrado")
        ticket.quantity_available += quantity
        self.repository.update(ticket_id, ticket)
