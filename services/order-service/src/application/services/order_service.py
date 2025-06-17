from logging import Logger
from fastapi import HTTPException
from src.domain.entities.order_entity import Order
from src.application.use_cases.create_order_use_case import CreateOrderUseCase
from src.application.use_cases.get_order_use_case import GetOrderUseCase
from src.application.use_cases.list_orders_use_case import ListOrdersUseCase
from src.application.clients.reservation_client import ReservationClient

class OrderService:

    def __init__(
        self,
        create_use_case: CreateOrderUseCase,
        get_use_case: GetOrderUseCase,
        list_use_case: ListOrdersUseCase,
        reservation_client: ReservationClient,
        logger: Logger,
    ):
        self.create_use_case = create_use_case
        self.get_use_case = get_use_case
        self.list_use_case = list_use_case
        self.reservation_client = reservation_client
        self.logger = logger

    async def create(self, order: Order) -> Order:

        reservations = self.reservation_client.get_user_reservations(order.user_id)

        valid_reservations = [r for r in reservations if not r.get("is_confirmed")]

        if not valid_reservations:
            raise ValueError("Nenhuma reserva válida encontrada.")

        for r in valid_reservations:
            self.reservation_client.confirm_reservation(r["reservation_id"])

        return await self.create_use_case.execute(order)

    def get(self, order_id: int) -> Order:
        result = self.get_use_case.execute(order_id)
        if not result:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return result

    def list(self):
        return self.list_use_case.execute()
