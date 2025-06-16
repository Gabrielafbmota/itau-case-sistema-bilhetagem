from pydantic import BaseModel

from typing import Optional


class ProductResponse(BaseModel):
    product_id: Optional[int] = None
    name: str
    description: str
    price: float
    stock: int


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductUpdate(ProductBase):
    name: Optional[str] = None  # type: ignore
    price: Optional[float] = None  # type: ignore
