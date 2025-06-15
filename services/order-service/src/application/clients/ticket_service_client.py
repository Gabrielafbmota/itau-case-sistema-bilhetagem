import httpx
from src.domain.entities.order_entity import Order
from src.core.config import get_env_var


class TicketServiceClient:
    def __init__(self):
        self.base_url = get_env_var("TICKET_SERVICE_URL")

    def generate_ticket_from_order(self, order: Order):
        if not order.products:
            raise ValueError("Pedido deve conter ao menos um produto para gerar ticket")

        payload = {
            "order_id": order.id,
            "user": {
                "id": order.user_id,
                "name": order.user_name,
                "email": order.user_email,
            },
            "event": {
                "id": order.event_id,
                "name": order.event_name,
                "location": order.event_location,
                "date": order.event_date.isoformat(),
            },
            "products": [
                {"name": p.name, "quantity": p.quantity, "price": p.price}
                for p in order.products
            ],
            "total_price": order.total_price,
        }

        try:
            response = httpx.post(
                f"{self.base_url}/tickets/from-order", json=payload, timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            raise RuntimeError(f"Erro de conexão com o ticket-service: {str(e)}")
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"Erro HTTP do ticket-service: {e.response.text}")
