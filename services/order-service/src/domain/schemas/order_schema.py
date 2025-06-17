from typing import List, Optional
from pydantic import BaseModel


class OrderItemSchema(BaseModel):
    ticket_id: int
    quantity: int
    unit_price: float


class OrderProductSchema(BaseModel):
    product_id: int
    quantity: int
    unit_price: float


class CreateOrderSchema(BaseModel):
    user_id: int
    event_id: int  # <-- ESSENCIAL
    items: List[OrderItemSchema]
    products: Optional[List[OrderProductSchema]] = []
    total: float


class OrderResponseSchema(BaseModel):
    id: int
    user_id: int
    total: float
    items: List[OrderItemSchema]
    products: List[OrderProductSchema]

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2
