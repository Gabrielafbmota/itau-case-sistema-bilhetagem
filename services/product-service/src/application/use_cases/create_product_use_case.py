from src.infrastructure.repositories.product_repository import ProductRepository
from src.domain.schemas.product_schema import ProductCreate


class CreateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_data: ProductCreate):
        return self.repository.create_product(product_data)
