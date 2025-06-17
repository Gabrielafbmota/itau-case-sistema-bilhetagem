from src.domain.interfaces.reservation_repository_interface import IReservationRepository


class GetReservationUseCase:
    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    def execute(self, reservation_id: int):
        return self.repository.get_by_id(reservation_id)
