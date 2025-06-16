from src.infrastructure.repositories.product_repository import ProductRepository


class ListProductByIdUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.repository = product_repository

    def execute(self, product_id: int, **kwargs):
        return self.repository.get_product_by_id(product_id)
