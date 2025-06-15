from abc import ABC, abstractmethod
from src.infrastructure.database.models.products_model import ProductsModel


class IProductsRepository(ABC):
    @abstractmethod
    def list_products(self) -> list[ProductsModel]: ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductsModel: ...
