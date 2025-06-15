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
        create_uc: CreateEventUseCase,
        get_uc: GetEventUseCase,
        list_uc: ListEventsUseCase,
        update_uc: UpdateEventUseCase,
        delete_uc: DeleteEventUseCase,
        logger: Logger,
    ):
        self.create_uc = create_uc
        self.get_uc = get_uc
        self.list_uc = list_uc
        self.update_uc = update_uc
        self.delete_uc = delete_uc
        self.logger = logger

    def create(self, event: Event) -> Event:
        try:
            return self.create_uc.execute(event)
        except Exception as e:
            self.logger.error(f"Erro ao criar evento: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar evento")

    def get(self, event_id: int) -> Event:
        event = self.get_uc.execute(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return event

    def list(self):
        return self.list_uc.execute()

    def update(self, event_id: int, event: Event):
        updated = self.update_uc.execute(event_id, event)
        if not updated:
            raise HTTPException(status_code=404, detail="Evento não encontrado")
        return updated

    def delete(self, event_id: int):
        self.delete_uc.execute(event_id)
