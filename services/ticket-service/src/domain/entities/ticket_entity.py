from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Ticket(BaseModel):
    id: Optional[int]
    event_id: int
    price: float
    quantity: int
    category: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
