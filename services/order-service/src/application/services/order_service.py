from logging import Logger
from fastapi import HTTPException
from src.domain.entities.order_entity import Order
from src.application.use_cases.create_order_use_case import CreateOrderUseCase
from src.application.use_cases.get_order_use_case import GetOrderUseCase
from src.application.use_cases.list_orders_use_case import ListOrdersUseCase


class OrderService:
    def __init__(
        self,
        create_uc: CreateOrderUseCase,
        get_uc: GetOrderUseCase,
        list_uc: ListOrdersUseCase,
        logger: Logger,
    ):
        self.create_uc = create_uc
        self.get_uc = get_uc
        self.list_uc = list_uc
        self.logger = logger

    def create(self, order: Order) -> Order:
        try:
            return self.create_uc.execute(order)
        except Exception as e:
            self.logger.error(f"Erro ao criar pedido: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar pedido")

    def get(self, order_id: int) -> Order:
        result = self.get_uc.execute(order_id)
        if not result:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return result

    def list(self):
        return self.list_uc.execute()
