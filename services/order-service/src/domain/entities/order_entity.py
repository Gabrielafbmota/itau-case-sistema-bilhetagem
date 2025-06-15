from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class OrderItem(BaseModel):
    ticket_id: int
    quantity: int
    unit_price: float


class OrderProduct(BaseModel):
    product_id: int
    quantity: int
    unit_price: float


from typing import List, Optional
from datetime import datetime


class Order:
    def __init__(
        self,
        user_id: int,
        event_id: int,
        product_ids: Optional[List[int]] = None,
        total_price: Optional[float] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        id: Optional[int] = None,
    ):
        self.id = id
        self.user_id = user_id
        self.event_id = event_id
        self.product_ids = product_ids or []
        self.total_price = total_price
        self.created_at = created_at
        self.updated_at = updated_at

        # Dados enriquecidos – NÃO persistidos no banco
        self.user_data: Optional[dict] = None
        self.event_data: Optional[dict] = None
        self.products_data: Optional[List[dict]] = []

    def __repr__(self):
        return (
            f"<Order(id={self.id}, user_id={self.user_id}, event_id={self.event_id})>"
        )
