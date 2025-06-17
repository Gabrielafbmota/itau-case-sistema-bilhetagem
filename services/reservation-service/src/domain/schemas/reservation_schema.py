from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CreateReservationSchema(BaseModel):
    user_id: int
    ticket_id: int
    quantity: int


class ReservationResponseSchema(BaseModel):
    reservation_id: int
    user_id: int
    ticket_id: int
    quantity: int
    reserved_at: datetime
    expires_at: Optional[datetime]
    is_confirmed: bool

    class Config:
        orm_mode = True
