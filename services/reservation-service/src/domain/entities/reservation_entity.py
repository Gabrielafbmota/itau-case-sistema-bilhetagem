from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Reservation(BaseModel):
    reservation_id: Optional[int] = None
    user_id: int
    ticket_id: int
    quantity: int
    reserved_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    is_confirmed: bool = False

    class Config:
        from_attributes = True
