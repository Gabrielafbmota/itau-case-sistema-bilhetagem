from sqlalchemy.orm import Session
from src.infrastructure.database.models.products_model import ProductsModel
from src.domain.repositories.product_repository import IProductsRepository
from src.domain.schemas.product_schema import ProductCreate, ProductUpdate
from fastapi import HTTPException


class ProductRepository(IProductsRepository):
    def __init__(self, db: Session):
        self.db = db

    def list_products(self) -> list[ProductsModel]:
        return self.db.query(ProductsModel).all()

    def get_product_by_id(self, product_id: int) -> ProductsModel:
        return (
            self.db.query(ProductsModel)
            .filter(ProductsModel.product_id == product_id)
            .first()
        )

    def create_product(self, product_data: ProductCreate):
        product = ProductsModel(**product_data.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update_product(self, product_id: int, product_data: ProductUpdate):
        product = (
            self.db.query(ProductsModel)
            .filter(ProductsModel.product_id == product_id)
            .first()
        )
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        for field, value in product_data.dict(exclude_unset=True).items():
            setattr(product, field, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int):
        product = (
            self.db.query(ProductsModel)
            .filter(ProductsModel.product_id == product_id)
            .first()
        )
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        self.db.delete(product)
        self.db.commit()
