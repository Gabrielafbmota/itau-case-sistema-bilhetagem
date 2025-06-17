import httpx
from src.core.config import get_env_var


class ProductClient:

    def __init__(self, logger):
        self.base_url = get_env_var("PRODUCT_SERVICE_URL")
        self.logger = logger

    def get_product(self, product_id: int) -> dict:
        try:
            response = httpx.get(f"{self.base_url}/products/{product_id}", timeout=5)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"Erro ao buscar produto {product_id} -> {str(e)}")
            raise Exception(f"Erro ao buscar produto {product_id}: {str(e)}")
