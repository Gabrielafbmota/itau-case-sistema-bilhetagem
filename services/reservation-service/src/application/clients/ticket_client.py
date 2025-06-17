import httpx
from src.core.config import get_env_var


class TicketClient:
    def __init__(self):
        self.base_url = get_env_var("TICKET_SERVICE_URL")

    def decrement_ticket_quantity(self, ticket_id: int, quantity: int):
        url = f"{self.base_url}/tickets/{ticket_id}/decrement"
        response = httpx.post(url, params={"quantity": quantity})
        response.raise_for_status()

    def increment_ticket_quantity(self, ticket_id: int, quantity: int):
        url = f"{self.base_url}/tickets/{ticket_id}/increment"
        response = httpx.post(url, params={"quantity": quantity})
        response.raise_for_status()
