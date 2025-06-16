from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.infrastructure.database.session import Base


class OrderProductModel(Base):
    __tablename__ = "order_products"

    order_product_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    order = relationship("OrderModel", back_populates="products")
