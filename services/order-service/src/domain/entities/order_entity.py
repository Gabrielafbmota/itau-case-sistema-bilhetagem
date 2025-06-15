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
        self.products_data: List[dict] = []

    def __repr__(self):
        return (
            f"<Order(id={self.id}, user_id={self.user_id}, event_id={self.event_id})>"
        )

    @property
    def user_name(self) -> str:
        return self.user_data.get("name", "") if self.user_data else ""

    @property
    def user_email(self) -> str:
        return self.user_data.get("email", "") if self.user_data else ""

    @property
    def event_name(self) -> str:
        return self.event_data.get("name", "") if self.event_data else ""

    @property
    def event_location(self) -> str:
        return self.event_data.get("location", "") if self.event_data else ""

    @property
    def event_date(self) -> datetime:
        date_str = self.event_data.get("date") if self.event_data else None
        return datetime.fromisoformat(date_str) if date_str else datetime.now()

    @property
    def products(self) -> List:
        return [
            {
                "name": p.get("name"),
                "quantity": p.get("quantity"),
                "price": p.get("price"),
            }
            for p in self.products_data or []
        ]
