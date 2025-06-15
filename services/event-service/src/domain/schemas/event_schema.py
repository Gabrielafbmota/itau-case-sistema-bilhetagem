from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateEventSchema(BaseModel):
    name: str
    description: Optional[str]
    location: str
    date: datetime
    capacity: int


class UpdateEventSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[datetime]
    capacity: Optional[int]
