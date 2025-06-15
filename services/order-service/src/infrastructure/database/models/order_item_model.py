from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.infrastructure.database.session import Base


class OrderItemModel(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    ticket_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    order = relationship("OrderModel", back_populates="items")
