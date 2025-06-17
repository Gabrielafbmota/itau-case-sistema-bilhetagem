from sqlalchemy import Column, Integer, Float, DateTime, func
from sqlalchemy.orm import relationship
from src.infrastructure.database.session import Base


class OrderModel(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship(
        "OrderItemModel", back_populates="order", cascade="all, delete-orphan"
    )
    products = relationship(
        "OrderProductModel", back_populates="order", cascade="all, delete-orphan"
    )
