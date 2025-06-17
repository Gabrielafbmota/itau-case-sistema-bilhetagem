from fastapi import HTTPException
from logging import Logger
from src.domain.entities.event_entity import Event
from src.application.use_cases.create_event_use_case import CreateEventUseCase
from src.application.use_cases.get_event_use_case import GetEventUseCase
from src.application.use_cases.list_events_use_case import ListEventsUseCase
from src.application.use_cases.update_event_use_case import UpdateEventUseCase
from src.application.use_cases.delete_event_use_case import DeleteEventUseCase


class EventService:

    def __init__(
        self,
        create_use_case: CreateEventUseCase,
        get_use_case: GetEventUseCase,
        list_use_case: ListEventsUseCase,
        update_use_case: UpdateEventUseCase,
        delete_use_case: DeleteEventUseCase,
        logger: Logger,
    ):
        self.create_use_case = create_use_case
        self.get_use_case = get_use_case
        self.list_use_case = list_use_case
        self.update_use_case = update_use_case
        self.delete_use_case = delete_use_case
        self.logger = logger

    def create(self, event: Event) -> Event:
        try:
            return self.create_use_case.execute(event)
        except Exception as e:
            self.logger.error(f"Erro ao criar evento: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar evento")

    def get(self, event_id: int) -> Event:
        event = self.get_use_case.execute(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return event

    def list(self):
        return self.list_use_case.execute()

    def update(self, event_id: int, event: Event):
        updated = self.update_use_case.execute(event_id, event)
        if not updated:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return updated

    def delete(self, event_id: int):
        self.delete_use_case.execute(event_id)
