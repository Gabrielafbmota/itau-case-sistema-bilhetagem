from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.core.logger import get_logger
from src.domain.entities.ticket_entity import Ticket
from src.domain.schemas.ticket_schema import (
    CreateTicketSchema,
    UpdateTicketSchema,
    TicketFromOrderSchema,
    TicketResponseSchema,
)
from src.infrastructure.repositories.ticket_repository import TicketRepository
from src.application.use_cases.create_ticket_use_case import CreateTicketUseCase
from src.application.use_cases.list_tickets_by_event_use_case import (
    ListTicketsByEventUseCase,
)
from src.infrastructure.database.session import DatabaseSession
from src.application.use_cases.get_ticket_use_case import GetTicketUseCase
from src.application.use_cases.update_ticket_use_case import UpdateTicketUseCase
from src.application.use_cases.delete_ticket_use_case import DeleteTicketUseCase
from src.application.services.ticket_service import TicketService
from src.application.use_cases.generate_ticket_from_order_use_case import (
    GenerateTicketFromOrderUseCase,
)
from fastapi.responses import FileResponse
import os

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_ticket_service(
    db: Session = Depends(DatabaseSession().get_session),
) -> TicketService:
    repo = TicketRepository(db)
    return TicketService(
        create_uc=CreateTicketUseCase(repo),
        list_uc=ListTicketsByEventUseCase(repo),
        get_uc=GetTicketUseCase(repo),
        update_uc=UpdateTicketUseCase(repo),
        delete_uc=DeleteTicketUseCase(repo),
        logger=get_logger(),
    )

@router.post("/", response_model=Ticket, status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket_data: CreateTicketSchema,
    service: TicketService = Depends(get_ticket_service),
):
    ticket = Ticket(**ticket_data.dict())
    return service.create(ticket)

@router.get("/event/{event_id}", response_model=List[Ticket])
def list_tickets_by_event(
    event_id: int, service: TicketService = Depends(get_ticket_service)
):
    return service.list_by_event(event_id)

@router.get("/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int, service: TicketService = Depends(get_ticket_service)):
    return service.get(ticket_id)

@router.put("/{ticket_id}", response_model=Ticket)
def update_ticket(
    ticket_id: int,
    ticket_data: UpdateTicketSchema,
    service: TicketService = Depends(get_ticket_service),
):
    ticket = Ticket(**ticket_data.dict(exclude_unset=True))
    return service.update(ticket_id, ticket)

@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ticket(ticket_id: int, service: TicketService = Depends(get_ticket_service)):
    service.delete(ticket_id)


# Nova rota para gerar ticket a partir do pedido
@router.post(
    "/from-order",
    response_model=TicketResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def generate_ticket_from_order(payload: TicketFromOrderSchema):
    use_case = GenerateTicketFromOrderUseCase()
    return use_case.execute(payload)


# Nova rota para recuperar PDF do ticket
@router.get("/{ticket_id}/pdf")
def get_ticket_pdf(ticket_id: str):
    filepath = f"tickets/ticket_{ticket_id}.pdf"
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Ticket não encontrado")
    return FileResponse(
        path=filepath, media_type="application/pdf", filename=os.path.basename(filepath)
    )
