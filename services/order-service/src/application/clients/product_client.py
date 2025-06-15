import httpx
from src.core.config import get_env_var


class ProductClient:
    def __init__(self):
        self.base_url = get_env_var("PRODUCT_SERVICE_URL")

    def get_product(self, product_id: int) -> dict:
        try:
            response = httpx.get(f"{self.base_url}/products/{product_id}", timeout=5)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise Exception(f"Erro ao buscar produto {product_id}: {str(e)}")
