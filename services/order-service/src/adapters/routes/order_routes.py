from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.core.logger import get_logger
from src.domain.schemas.order_schema import CreateOrderSchema, OrderResponseSchema
from src.infrastructure.repositories.order_repository import OrderRepository
from src.infrastructure.database.session import DatabaseSession
from src.application.services.order_service import OrderService
from src.application.use_cases.create_order_use_case import CreateOrderUseCase
from src.application.use_cases.get_order_use_case import GetOrderUseCase
from src.application.use_cases.list_orders_use_case import ListOrdersUseCase

# Clients HTTP
from src.application.clients.user_client import UserClient
from src.application.clients.event_client import EventClient
from src.application.clients.product_client import ProductClient

from src.domain.entities.order_entity import Order


router = APIRouter(prefix="/orders", tags=["Orders"])
logger = get_logger(__name__)

def get_service(db: Session = Depends(DatabaseSession().get_session)) -> OrderService:
    repository = OrderRepository(db)

    # Instancia os clients HTTP
    user_client = UserClient()
    event_client = EventClient()
    product_client = ProductClient()

    return OrderService(
        create_uc=CreateOrderUseCase(
            repository,
            user_client=user_client,
            event_client=event_client,
            product_client=product_client,
        ),
        get_uc=GetOrderUseCase(repository),
        list_uc=ListOrdersUseCase(repository),
        logger=logger,
    )


@router.post(
    "/", response_model=OrderResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_order(
    payload: CreateOrderSchema, service: OrderService = Depends(get_service)
):
    order = Order(**payload.model_dump())
    return service.create(order)


@router.get("/{order_id}", response_model=OrderResponseSchema)
def get_order(order_id: int, service: OrderService = Depends(get_service)):
    return service.get(order_id)


@router.get("/", response_model=List[OrderResponseSchema])
def list_orders(service: OrderService = Depends(get_service)):
    return service.list()
