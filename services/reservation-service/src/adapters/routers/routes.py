from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.core.logger import get_logger
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.reservation_repository import ReservationRepository
from src.application.use_cases.create_reservation_use_case import (
    CreateReservationUseCase,
)
from src.application.use_cases.get_reservations_use_case import GetReservationUseCase
from src.application.use_cases.list_reservation_use_case import (
    ListReservationsByUserUseCase,
)
from src.application.use_cases.cancel_reservation_use_case import (
    CancelReservationUseCase,
)
from src.application.use_cases.confirm_reservation_use_case import (
    ConfirmReservationUseCase,
)
from src.application.clients.ticket_client import TicketClient
from src.application.services.reservation_service import ReservationService
from src.domain.entities.reservation_entity import Reservation
from src.domain.schemas.reservation_schema import (
    CreateReservationSchema,
    ReservationResponseSchema,
)

router = APIRouter(prefix="/reservations", tags=["Reservations"])


def get_reservation_service(
    db: Session = Depends(DatabaseSession().get_session),
) -> ReservationService:
    repository = ReservationRepository(db)
    return ReservationService(
        create_use_case=CreateReservationUseCase(repository),
        get_use_case=GetReservationUseCase(repository),
        list_by_user_use_case=ListReservationsByUserUseCase(repository),
        cancel_use_case=CancelReservationUseCase(repository),
        confirm_use_case=ConfirmReservationUseCase(repository),
        logger=get_logger(),
        ticket_client=TicketClient(),
    )


@router.post(
    "/", response_model=ReservationResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_reservation(
    reservation_data: CreateReservationSchema,
    service: ReservationService = Depends(get_reservation_service),
):
    reservation = Reservation(**reservation_data.dict())
    return service.create(reservation)


@router.get("/{reservation_id}", response_model=ReservationResponseSchema)
def get_reservation(
    reservation_id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    return service.get(reservation_id)


@router.get("/user/{user_id}", response_model=List[ReservationResponseSchema])
def list_reservations_by_user(
    user_id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    return service.list_by_user(user_id)


@router.post("/{reservation_id}/cancel", status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(
    reservation_id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    service.cancel(reservation_id)


@router.post("/{reservation_id}/confirm", status_code=status.HTTP_200_OK)
def confirm_reservation(
    reservation_id: int,
    service: ReservationService = Depends(get_reservation_service),
):
    service.confirm(reservation_id)
