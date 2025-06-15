from src.infrastructure.repositories.product_repository import ProductRepository


class ListProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.repository = product_repository

    def execute(self):
        return self.repository.list_products()
