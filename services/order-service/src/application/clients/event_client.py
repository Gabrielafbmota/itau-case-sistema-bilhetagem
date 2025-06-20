import httpx
from src.core.config import get_env_var


class EventClient:

    def __init__(self, logger):
        self.base_url = get_env_var("EVENT_SERVICE_URL")
        self.logger = logger

    def get_event(self, event_id: int) -> dict:
        try:
            response = httpx.get(f"{self.base_url}/events/{event_id}", timeout=5)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"Erro ao buscar evento {event_id} -> {str(e)}")
            raise Exception(f"Erro ao buscar evento {event_id}: {str(e)}")
