from sqlalchemy import Column, Integer, String, DateTime, func
from src.infrastructure.database.session import Base


class ProductsModel(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "bilheteria_schema"}

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, name='{self.name}')>"
