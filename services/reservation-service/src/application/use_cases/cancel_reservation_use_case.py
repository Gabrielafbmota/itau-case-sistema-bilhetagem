from src.domain.interfaces.reservation_repository_interface import IReservationRepository


class CancelReservationUseCase:
    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    def execute(self, reservation_id: int):
        return self.repository.cancel(reservation_id)
