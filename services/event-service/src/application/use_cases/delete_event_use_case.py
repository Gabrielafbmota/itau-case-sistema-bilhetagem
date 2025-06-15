from src.domain.interfaces.event_repository_interface import EventRepositoryInterface


class DeleteEventUseCase:
    def __init__(self, repository: EventRepositoryInterface):
        self.repository = repository

    def execute(self, event_id: int) -> None:
        self.repository.delete(event_id)
