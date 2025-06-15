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


class TicketService:
    def __init__(
        self,
        create_uc: CreateTicketUseCase,
        list_uc: ListTicketsByEventUseCase,
        get_uc: GetTicketUseCase,
        update_uc: UpdateTicketUseCase,
        delete_uc: DeleteTicketUseCase,
        logger: Logger,
    ):
        self.create_uc = create_uc
        self.list_uc = list_uc
        self.get_uc = get_uc
        self.update_uc = update_uc
        self.delete_uc = delete_uc
        self.logger = logger

    def create(self, ticket: Ticket):
        try:
            return self.create_uc.execute(ticket)
        except Exception as e:
            self.logger.error(f"Erro ao criar ticket: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar ticket")

    def list_by_event(self, event_id: int):
        return self.list_uc.execute(event_id)

    def get(self, ticket_id: int):
        ticket = self.get_uc.execute(ticket_id)
        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket não encontrado")
        return ticket

    def update(self, ticket_id: int, ticket: Ticket):
        result = self.update_uc.execute(ticket_id, ticket)
        if not result:
            raise HTTPException(status_code=404, detail="Ticket não encontrado")
        return result

    def delete(self, ticket_id: int):
        self.delete_uc.execute(ticket_id)
