from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Ticket(BaseModel):
    ticket_id: Optional[int] = None
    event_id: int
    type: Optional[str]
    price: float
    quantity_total: int
    quantity_available: int

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True
        from_attributes = True
