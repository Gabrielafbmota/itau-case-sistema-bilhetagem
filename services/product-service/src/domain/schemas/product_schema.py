from pydantic import BaseModel

from typing import Optional


class ProductResponse(BaseModel):
    product_id: int
    name: str
    description: str
    price: float


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
