from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserDataSchema(BaseModel):
    user_id: int
    name: str
    email: str


class EventDataSchema(BaseModel):
    event_id: int
    title: str
    date: datetime
    location: str


class ProductDataSchema(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int


class TicketFromOrderSchema(BaseModel):
    ticket_id: int
    order_id: int
    user: UserDataSchema
    event: EventDataSchema
    products: List[ProductDataSchema]
    total_price: float


class TicketResponseSchema(BaseModel):
    ticket_id: int
    order_id: int
    pdf_path: str


class CreateTicketSchema(BaseModel):
    event_id: int
    price: float
    quantity_total: int
    quantity_available: int
    type: str


class UpdateTicketSchema(BaseModel):
    price: Optional[float]
    quantity_total: Optional[int]
    quantity_available: Optional[int]
    type: Optional[str]


class TicketSchema(BaseModel):
    ticket_id: int
    event_id: int
    price: float
    quantity_total: int
    quantity_available: int
    type: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
