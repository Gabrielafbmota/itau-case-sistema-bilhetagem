from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.product_repository import ProductRepository
from src.application.services.product_service import ProductsService
from src.application.use_cases.list_products_use_case import ListProductUseCase
from src.application.use_cases.create_product_use_case import CreateProductUseCase
from src.application.use_cases.update_product_use_case import UpdateProductUseCase
from src.application.use_cases.delete_product_use_case import DeleteProductUseCase
from src.application.use_cases.list_product_by_id_use_case import ListProductByIdUseCase
from src.domain.schemas.product_schema import ProductCreate, ProductUpdate
from src.middlewares.auth import get_current_user, get_current_admin_user
from src.core.logger import get_logger

products_router = APIRouter(prefix="/products", tags=["Products"])

logger = get_logger()


def get_products_services(db: Session = Depends(DatabaseSession().get_session)):
    repo = ProductRepository(db)
    return ProductsService(
        list_use_case=ListProductUseCase(repo),
        create_use_case=CreateProductUseCase(repo),
        update_use_case=UpdateProductUseCase(repo),
        delete_use_case=DeleteProductUseCase(repo),
        list_product_by_id_use_case=ListProductByIdUseCase(repo),
        logger=logger,
    )


@products_router.get("/{product_id}")
def get_product(
    product_id: int, service: ProductsService = Depends(get_products_services)
):
    try:
        return service.list_product_by_id(product_id)
    except HTTPException as e:
        raise e


@products_router.get("/")
def get_products(service: ProductsService = Depends(get_products_services)):
    try:
        return service.list_products()
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Erro ao buscar produtos: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")


@products_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    product: ProductCreate, service: ProductsService = Depends(get_products_services)
):
    try:
        return service.create_product(product)
    except Exception as e:
        logger.error(f"Erro ao criar produto: {e}")
        raise HTTPException(status_code=500, detail="Erro ao criar produto")


@products_router.put("/{id}", dependencies=[Depends(get_current_admin_user)])
def update_product(
    id: int,
    product: ProductUpdate,
    service: ProductsService = Depends(get_products_services),
):
    try:
        return service.update_product(id, product)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Erro ao atualizar produto {id}: {e}")
        raise HTTPException(status_code=500, detail="Erro ao atualizar produto")


@products_router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product(id: int, service: ProductsService = Depends(get_products_services)):
    try:
        service.delete_product(id)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Erro ao deletar produto {id}: {e}")
        raise HTTPException(status_code=500, detail="Erro ao deletar produto")
