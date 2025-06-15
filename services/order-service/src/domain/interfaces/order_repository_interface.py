from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.order_entity import Order


class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create(self, order: Order) -> Order:
        """Cria um novo pedido"""
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        """Busca um pedido por ID"""
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        """Lista todos os pedidos"""
        pass
