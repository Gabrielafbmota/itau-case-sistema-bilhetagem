from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Event(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    location: str
    date: datetime
    capacity: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
