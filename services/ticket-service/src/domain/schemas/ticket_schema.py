from pydantic import BaseModel
from typing import Optional


class CreateTicketSchema(BaseModel):
    event_id: int
    price: float
    quantity: int
    category: str


class UpdateTicketSchema(BaseModel):
    price: Optional[float]
    quantity: Optional[int]
    category: Optional[str]
