from src.infrastructure.database.session import DatabaseSession
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.core.logger import get_logger
from src.domain.schemas.event_schema import CreateEventSchema, UpdateEventSchema
from src.domain.entities.event_entity import Event
from src.infrastructure.repositories.event_repository import EventRepository
from src.application.use_cases.create_event_use_case import CreateEventUseCase
from src.application.use_cases.get_event_use_case import GetEventUseCase
from src.application.use_cases.list_events_use_case import ListEventsUseCase
from src.application.use_cases.update_event_use_case import UpdateEventUseCase
from src.application.use_cases.delete_event_use_case import DeleteEventUseCase
from src.application.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["Eventos"])


def get_event_service(
    db: Session = Depends(DatabaseSession().get_session),
) -> EventService:
    repository = EventRepository(db)
    return EventService(
        create_uc=CreateEventUseCase(repository),
        get_uc=GetEventUseCase(repository),
        list_uc=ListEventsUseCase(repository),
        update_uc=UpdateEventUseCase(repository),
        delete_uc=DeleteEventUseCase(repository),
        logger=get_logger(),
    )


@router.post("/", response_model=Event, status_code=status.HTTP_201_CREATED)
def create_event(
    event_data: CreateEventSchema, service: EventService = Depends(get_event_service)
):
    event = Event(**event_data.dict())
    return service.create(event)


@router.get("/", response_model=List[Event])
def list_events(service: EventService = Depends(get_event_service)):
    return service.list()


@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int, service: EventService = Depends(get_event_service)):
    return service.get(event_id)


@router.put("/{event_id}", response_model=Event)
def update_event(
    event_id: int,
    event_data: UpdateEventSchema,
    service: EventService = Depends(get_event_service),
):
    event = Event(**event_data.dict(exclude_unset=True))
    return service.update(event_id, event)


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int, service: EventService = Depends(get_event_service)):
    service.delete(event_id)
