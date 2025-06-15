from src.infrastructure.repositories.product_repository import ProductRepository
from fastapi import HTTPException


class DeleteProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: int):
        product = self.repository.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        self.repository.delete_product(product_id)
