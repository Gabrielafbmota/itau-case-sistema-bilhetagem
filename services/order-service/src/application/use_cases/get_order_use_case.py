from typing import Optional
from src.domain.entities.order_entity import Order
from src.domain.interfaces.order_repository_interface import OrderRepositoryInterface


class GetOrderUseCase:
    def __init__(self, repository: OrderRepositoryInterface):
        self.repository = repository

    def execute(self, order_id: int) -> Optional[Order]:
        return self.repository.get_by_id(order_id)
