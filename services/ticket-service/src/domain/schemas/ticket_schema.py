# src/domain/schemas/ticket_schema.py
from pydantic import BaseModel
from typing import List


class UserDataSchema(BaseModel):
    id: int
    name: str
    email: str


class EventDataSchema(BaseModel):
    id: int
    title: str
    date: str  # Pode ser ajustado para datetime se necessário


class ProductDataSchema(BaseModel):
    id: int
    name: str
    price: float


class TicketFromOrderSchema(BaseModel):
    order_id: int
    user: UserDataSchema
    event: EventDataSchema
    products: List[ProductDataSchema]
    total_price: float


class TicketResponseSchema(BaseModel):
    ticket_id: str
    order_id: int
    pdf_path: str


class CreateTicketSchema(BaseModel):
    event_id: int
    price: float
    quantity: int
    category: str


class UpdateTicketSchema(BaseModel):
    price: Optional[float]
    quantity: Optional[int]
    category: Optional[str]
