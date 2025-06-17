import httpx
from typing import List
from src.core.config import get_env_var


class ReservationClient:
    def __init__(self, logger):
        base_url = get_env_var("RESERVATION_SERVICE_URL")
        self.base_url = base_url.rstrip("/")
        self.logger = logger

    def get_user_reservations(self, user_id: int) -> List[dict]:
        try:
            response = httpx.get(f"{self.base_url}/reservations/user/{user_id}")
            response.raise_for_status()
            return response.json()

        except httpx.HTTPError as e:
            self.logger.error(
                f"Erro ao buscar reservas do usuário {user_id} -> {str(e)}"
            )
            raise Exception(f"Erro ao buscar reservas do usuário {user_id}: {str(e)}")

    def confirm_reservation(self, reservation_id: int) -> None:
        try:
            response = httpx.post(
                f"{self.base_url}/reservations/{reservation_id}/confirm"
            )
            response.raise_for_status()
        except httpx.HTTPError as e:
            self.logger.error(f"Erro ao confirmar reserva {reservation_id} -> {str(e)}")
            raise Exception(f"Erro ao confirmar reserva {reservation_id}: {str(e)}")
