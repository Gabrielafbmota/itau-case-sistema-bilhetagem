import asyncio
import httpx
from src.domain.entities.order_entity import Order
from src.core.config import get_env_var


class TicketServiceClient:

    def __init__(self, logger):
        self.base_url = get_env_var("TICKET_SERVICE_URL")
        self.logger = logger

    async def _send_ticket_request(self, client: httpx.AsyncClient, payload: dict):
        try:
            response = await client.post(
                f"{self.base_url}/tickets/from-order", json=payload, timeout=10.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            self.logger.error(f"Erro de conexão com o ticket-service: {str(e)}")
            raise Exception(f"Erro de conexão com o ticket-service: {str(e)}")
        except httpx.HTTPStatusError as e:
            self.logger.error(f"Erro HTTP do ticket-service: {e.response.text}")
            raise Exception(f"Erro HTTP do ticket-service: {e.response.text}")

    async def generate_ticket_from_order(self, order: Order):
        if not order.items:
            raise ValueError(
                "Pedido deve conter ao menos um item de ingresso para gerar ticket"
            )

        async with httpx.AsyncClient() as client:
            tasks = []
            for i in order.items:
                payload = {
                    "ticket_id": i.ticket_id,
                    "order_id": order.order_id,
                    "user": {
                        "user_id": order.user_id,
                        "name": order.user_name,
                        "email": order.user_email,
                    },
                    "event": {
                        "event_id": order.event_id,
                        "name": order.event_name,
                        "title": order.event_name,
                        "location": order.event_location,
                        "date": order.event_date.isoformat(),
                    },
                    "products": order.formatted_products,
                    "total_price": order.total_price,
                }

                tasks.append(self._send_ticket_request(client, payload))

            return await asyncio.gather(*tasks)
