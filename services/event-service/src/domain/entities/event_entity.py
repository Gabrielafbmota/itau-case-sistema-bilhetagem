from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Event(BaseModel):
    event_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_time: datetime
    end_time: datetime
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
