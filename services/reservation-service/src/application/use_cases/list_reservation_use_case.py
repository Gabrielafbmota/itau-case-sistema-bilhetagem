from src.domain.interfaces.reservation_repository_interface import IReservationRepository


class ListReservationsByUserUseCase:
    def __init__(self, repository: IReservationRepository):
        self.repository = repository

    def execute(self, user_id: int):
        return self.repository.list_by_user(user_id)
