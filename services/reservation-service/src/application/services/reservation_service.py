from logging import Logger
from src.domain.entities.reservation_entity import Reservation
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
from fastapi import HTTPException


class ReservationService:
    def __init__(
        self,
        create_use_case: CreateReservationUseCase,
        get_use_case: GetReservationUseCase,
        list_by_user_use_case: ListReservationsByUserUseCase,
        cancel_use_case: CancelReservationUseCase,
        confirm_use_case: ConfirmReservationUseCase,
        logger: Logger,
        ticket_client: TicketClient,
    ):
        self.create_use_case = create_use_case
        self.get_use_case = get_use_case
        self.list_by_user_use_case = list_by_user_use_case
        self.cancel_use_case = cancel_use_case
        self.confirm_use_case = confirm_use_case
        self.logger = logger
        self.ticket_client = ticket_client

    def create(self, reservation: Reservation) -> Reservation:
        self.logger.info(f"Criando reserva para o ticket {reservation.ticket_id}")
        created = self.create_use_case.execute(reservation)

        self.ticket_client.decrement_ticket_quantity(
            ticket_id=reservation.ticket_id, quantity=reservation.quantity
        )
        return created

    def cancel(self, reservation_id: int):
        self.logger.info(f"Cancelando reserva {reservation_id}")
        reservation = self.get(reservation_id)
        self.ticket_client.increment_ticket_quantity(
            ticket_id=reservation.ticket_id, quantity=reservation.quantity
        )
        self.cancel_use_case.execute(reservation_id)

    def get(self, reservation_id: int) -> Reservation:
        self.logger.info(f"Buscando reserva {reservation_id}")
        reservation = self.get_use_case.execute(reservation_id)
        if reservation is None:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return reservation

    def list_by_user(self, user_id: int):
        self.logger.info(f"Listando reservas do usuário {user_id}")
        return self.list_by_user_use_case.execute(user_id)

    def confirm(self, reservation_id: int):
        self.logger.info(f"Confirmando reserva {reservation_id}")
        self.confirm_use_case.execute(reservation_id)
