from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.event_entity import Event
from src.domain.interfaces.event_repository_interface import EventRepositoryInterface
from src.infrastructure.database.models.event_model import EventModel


class EventRepository(EventRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(self, event: Event) -> Event:
        event_model = EventModel(**event.dict(exclude_unset=True))
        self.db.add(event_model)
        self.db.commit()
        self.db.refresh(event_model)
        return Event.from_orm(event_model)

    def get_by_id(self, event_id: int) -> Optional[Event]:
        event = (
            self.db.query(EventModel).filter(EventModel.event_id == event_id).first()
        )
        return Event.from_orm(event) if event else None

    def list_all(self) -> List[Event]:
        events = self.db.query(EventModel).all()
        return [Event.from_orm(e) for e in events]

    def update(self, event_id: int, event: Event) -> Optional[Event]:
        event_model = (
            self.db.query(EventModel).filter(EventModel.event_id == event_id).first()
        )
        if not event_model:
            return None
        for field, value in event.dict(exclude_unset=True).items():
            setattr(event_model, field, value)
        self.db.commit()
        self.db.refresh(event_model)
        return Event.from_orm(event_model)

    def delete(self, event_id: int) -> None:
        event = (
            self.db.query(EventModel).filter(EventModel.event_id == event_id).first()
        )
        if event:
            self.db.delete(event)
            self.db.commit()
