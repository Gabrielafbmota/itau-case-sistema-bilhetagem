from src.domain.entities.order_entity import Order
from src.domain.interfaces.order_repository_interface import OrderRepositoryInterface
from src.application.clients.user_client import UserClient
from src.application.clients.event_client import EventClient
from src.application.clients.product_client import ProductClient


class CreateOrderUseCase:
    def __init__(
        self,
        repository: OrderRepositoryInterface,
        user_client: UserClient,
        event_client: EventClient,
        product_client: ProductClient,
    ):
        self.repository = repository
        self.user_client = user_client
        self.event_client = event_client
        self.product_client = product_client

    def execute(self, order: Order) -> Order:
        # Enriquecimento via serviços externos
        user_data = self.user_client.get_user(order.user_id)
        event_data = self.event_client.get_event(order.event_id)

        product_details = []
        for products in order.products:

            product = self.product_client.get_product(products.product_id)
            product_details.append(product)

        # (opcional) você pode atribuir esses dados ao order para uso posterior
        order.user_data = user_data
        order.event_data = event_data
        order.products_data = product_details

        # Persiste apenas o que for necessário no banco
        return self.repository.create(order)
