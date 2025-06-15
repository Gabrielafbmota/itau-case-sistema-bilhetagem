from logging import Logger
from fastapi import HTTPException
from src.application.use_cases.list_products_use_case import ListProductUseCase
from src.application.use_cases.create_product_use_case import CreateProductUseCase
from src.application.use_cases.update_product_use_case import UpdateProductUseCase
from src.application.use_cases.delete_product_use_case import DeleteProductUseCase
from src.domain.schemas.product_schema import ProductCreate, ProductUpdate


class ProductsService:
    def __init__(
        self,
        list_use_case: ListProductUseCase,
        create_use_case: CreateProductUseCase,
        update_use_case: UpdateProductUseCase,
        delete_use_case: DeleteProductUseCase,
        logger: Logger,
    ) -> None:
        self.list_use_case = list_use_case
        self.create_use_case = create_use_case
        self.update_use_case = update_use_case
        self.delete_use_case = delete_use_case
        self.logger = logger

    def list_products(self):
        try:
            products = self.list_use_case.execute()
            if not products:
                raise HTTPException(status_code=404, detail="Nenhum produto encontrado")
            return products
        except Exception as e:
            self.logger.error(f"Erro ao buscar produtos: {e}")
            raise HTTPException(status_code=500, detail="Erro interno do servidor")

    def create_product(self, product_data: ProductCreate):
        try:
            return self.create_use_case.execute(product_data)
        except Exception as e:
            self.logger.error(f"Erro ao criar produto: {e}")
            raise HTTPException(status_code=500, detail="Erro ao criar produto")

    def update_product(self, product_id: int, product_data: ProductUpdate):
        try:
            return self.update_use_case.execute(product_id, product_data)
        except Exception as e:
            self.logger.error(f"Erro ao atualizar produto {product_id}: {e}")
            raise HTTPException(status_code=500, detail="Erro ao atualizar produto")

    def delete_product(self, product_id: int):
        try:
            self.delete_use_case.execute(product_id)
        except Exception as e:
            self.logger.error(f"Erro ao deletar produto {product_id}: {e}")
            raise HTTPException(status_code=500, detail="Erro ao deletar produto")
