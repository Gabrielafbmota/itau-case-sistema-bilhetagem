from fastapi import HTTPException
from logging import Logger
from src.domain.entities.ticket_entity import Ticket
from src.application.use_cases.create_ticket_use_case import CreateTicketUseCase
from src.application.use_cases.list_tickets_by_event_use_case import (
    ListTicketsByEventUseCase,
)
from src.application.use_cases.get_ticket_use_case import GetTicketUseCase
from src.application.use_cases.update_ticket_use_case import UpdateTicketUseCase
from src.application.use_cases.delete_ticket_use_case import DeleteTicketUseCase
from src.application.use_cases.increment_ticket_stock_use_case import (
    IncrementTicketStockUseCase,
)
from src.application.use_cases.decrement_ticket_stock_use_case import (
    DecrementTicketStockUseCase,
)

class TicketService:

    def __init__(
        self,
        create_use_case: CreateTicketUseCase,
        list_use_case: ListTicketsByEventUseCase,
        get_use_case: GetTicketUseCase,
        update_use_case: UpdateTicketUseCase,
        delete_use_case: DeleteTicketUseCase,
        increment_use_case: IncrementTicketStockUseCase,
        decrement_use_case: DecrementTicketStockUseCase,
        logger: Logger,
    ):
        self.create_use_case = create_use_case
        self.list_use_case = list_use_case
        self.get_use_case = get_use_case
        self.update_use_case = update_use_case
        self.delete_use_case = delete_use_case
        self.logger = logger
        self.increment_use_case = increment_use_case
        self.decrement_use_case = decrement_use_case

    def create(self, ticket: Ticket):
        try:
            return self.create_use_case.execute(ticket)
        except Exception as e:
            self.logger.error(f"Erro ao criar ticket: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar ticket")

    def list_by_event(self, event_id: int):
        return self.list_use_case.execute(event_id)

    def get(self, ticket_id: int):
        ticket = self.get_use_case.execute(ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket não encontrado")
        return ticket

    def update(self, ticket_id: int, ticket: Ticket):
        result = self.update_use_case.execute(ticket_id, ticket)
        if not result:
            raise HTTPException(status_code=404, detail="Ticket não encontrado")
        return result

    def delete(self, ticket_id: int):
        self.delete_use_case.execute(ticket_id)

    def increment_quantity(self, ticket_id: int, quantity: int):
        self.logger.info(f"Incrementando {quantity} no ticket {ticket_id}")
        self.increment_use_case.execute(ticket_id, quantity)

    def decrement_quantity(self, ticket_id: int, quantity: int):
        self.logger.info(f"Decrementando {quantity} do ticket {ticket_id}")
        self.decrement_use_case.execute(ticket_id, quantity)
