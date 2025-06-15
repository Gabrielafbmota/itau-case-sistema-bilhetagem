from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.ticket_entity import Ticket
from src.domain.interfaces.ticket_repository_interface import TicketRepositoryInterface
from src.infrastructure.database.models.ticket_model import TicketModel


class TicketRepository(TicketRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket: Ticket) -> Ticket:
        ticket_model = TicketModel(**ticket.dict(exclude_unset=True))
        self.db.add(ticket_model)
        self.db.commit()
        self.db.refresh(ticket_model)
        return Ticket.from_orm(ticket_model)

    def get_by_id(self, ticket_id: int) -> Optional[Ticket]:
        ticket = self.db.query(TicketModel).filter(TicketModel.id == ticket_id).first()
        return Ticket.from_orm(ticket) if ticket else None

    def list_by_event(self, event_id: int) -> List[Ticket]:
        tickets = (
            self.db.query(TicketModel).filter(TicketModel.event_id == event_id).all()
        )
        return [Ticket.from_orm(t) for t in tickets]

    def update(self, ticket_id: int, ticket: Ticket) -> Optional[Ticket]:
        ticket_model = (
            self.db.query(TicketModel).filter(TicketModel.id == ticket_id).first()
        )
        if not ticket_model:
            return None
        for field, value in ticket.dict(exclude_unset=True).items():
            setattr(ticket_model, field, value)
        self.db.commit()
        self.db.refresh(ticket_model)
        return Ticket.from_orm(ticket_model)

    def delete(self, ticket_id: int) -> None:
        ticket = self.db.query(TicketModel).filter(TicketModel.id == ticket_id).first()
        if ticket:
            self.db.delete(ticket)
            self.db.commit()
