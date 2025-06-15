from typing import List
from src.domain.entities.order_entity import Order
from src.domain.interfaces.order_repository_interface import OrderRepositoryInterface


class ListOrdersUseCase:
    def __init__(self, repository: OrderRepositoryInterface):
        self.repository = repository

    def execute(self) -> List[Order]:
        return self.repository.list_all()
