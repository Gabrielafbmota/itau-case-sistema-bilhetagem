from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateEventSchema(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: datetime
    end_time: datetime
    created_by: int


class UpdateEventSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    created_by: Optional[int] = None


class EventResponseSchema(BaseModel):
    event_id: int
    title: str
    description: Optional[str]
    location: Optional[str]
    start_time: datetime
    end_time: datetime
    created_by: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
