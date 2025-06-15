from typing import List, Optional
from sqlalchemy.orm import Session

from src.domain.entities.order_entity import Order
from src.domain.interfaces.order_repository_interface import OrderRepositoryInterface
from src.domain.schemas.order_schema import CreateOrderSchema
from src.infrastructure.database.models.order_model import OrderModel
from src.infrastructure.database.models.order_item_model import OrderItemModel
from src.infrastructure.database.models.order_product_model import OrderProductModel


class OrderRepository(OrderRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def create(self, order: Order) -> Order:
        db_order = OrderModel(user_id=order.user_id, total=order.total)
        self.db.add(db_order)
        self.db.flush()  # Garante que o ID seja atribuído

        # Adiciona os tickets (itens)
        for item in order.items:
            db_item = OrderItemModel(
                order_id=db_order.id,
                ticket_id=item.ticket_id,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            self.db.add(db_item)

        # Adiciona os produtos adicionais
        for product in order.products:
            db_product = OrderProductModel(
                order_id=db_order.id,
                product_id=product.product_id,
                quantity=product.quantity,
                unit_price=product.unit_price,
            )
            self.db.add(db_product)

        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_by_id(self, order_id: int) -> Optional[OrderModel]:
        return self.db.query(OrderModel).filter(OrderModel.id == order_id).first()

    def list_all(self) -> List[OrderModel]:
        return self.db.query(OrderModel).all()
