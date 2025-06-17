from src.domain.entities.order_entity import Order
from src.domain.interfaces.order_repository_interface import OrderRepositoryInterface
from src.application.clients.user_client import UserClient
from src.application.clients.event_client import EventClient
from src.application.clients.product_client import ProductClient
from src.application.clients.ticket_service_client import TicketServiceClient

class CreateOrderUseCase:

    def __init__(
        self,
        repository: OrderRepositoryInterface,
        user_client: UserClient,
        event_client: EventClient,
        product_client: ProductClient,
        ticket_client: TicketServiceClient,
        logger,
    ):
        self.repository = repository
        self.user_client = user_client
        self.event_client = event_client
        self.product_client = product_client
        self.ticket_client = ticket_client
        self.logger = logger

    async def execute(self, order: Order) -> Order:

        user_data = self.user_client.get_user(order.user_id)
        event_data = self.event_client.get_event(order.event_id)

        product_details = []
        for product_item in order.products:
            product = self.product_client.get_product(product_item.product_id)
            product_details.append(product)

        order.user_data = user_data
        order.event_data = event_data
        order.products_data = [
            {
                "product_id": p["product_id"],
                "name": p["name"],
                "quantity": op.quantity,
                "price": op.unit_price,
            }
            for p, op in zip(product_details, order.products)
        ]

        created_order = self.repository.create(order)
        order.order_id = created_order.order_id
        self.logger.info(f"Pedido criado com sucesso. ID: {order.order_id}")

        await self.ticket_client.generate_ticket_from_order(order=order)

        return order
