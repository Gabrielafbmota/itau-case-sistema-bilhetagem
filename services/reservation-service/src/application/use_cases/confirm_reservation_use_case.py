from src.domain.interfaces.reservation_repository_interface import IReservationRepository


class ConfirmReservationUseCase:
    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    def execute(self, reservation_id: int):
        return self.repository.confirm(reservation_id)
