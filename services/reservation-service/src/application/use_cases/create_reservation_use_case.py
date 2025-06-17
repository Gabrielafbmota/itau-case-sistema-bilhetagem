from src.domain.entities.reservation_entity import Reservation
from src.domain.interfaces.reservation_repository_interface import IReservationRepository


class CreateReservationUseCase:
    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    def execute(self, reservation: Reservation) -> Reservation:
        return self.repository.create(reservation)
