from src.infrastructure.repositories.product_repository import ProductRepository
from src.domain.schemas.product_schema import ProductUpdate
from fastapi import HTTPException


class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int, product_data: ProductUpdate):
        product = self.repository.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return self.repository.update_product(product_id, product_data)
