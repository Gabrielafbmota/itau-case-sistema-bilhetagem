from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from src.core.logger import get_logger
from src.domain.schemas.order_schema import CreateOrderSchema, OrderResponseSchema
from src.infrastructure.repositories.order_repository import OrderRepository
from src.infrastructure.database.session import DatabaseSession
from src.application.services.order_service import OrderService
from src.application.use_cases.create_order_use_case import CreateOrderUseCase
from src.application.use_cases.get_order_use_case import GetOrderUseCase
from src.application.use_cases.list_orders_use_case import ListOrdersUseCase

from src.application.clients.user_client import UserClient
from src.application.clients.event_client import EventClient
from src.application.clients.product_client import ProductClient
from src.application.clients.reservation_client import ReservationClient
from src.application.clients.ticket_service_client import TicketServiceClient

from src.domain.entities.order_entity import Order


router = APIRouter(prefix="/orders", tags=["Orders"])
logger = get_logger(__name__)

def get_service(db: Session = Depends(DatabaseSession().get_session)) -> OrderService:
    repository = OrderRepository(db)
    ticket_client = TicketServiceClient(logger)
    user_client = UserClient(logger)
    event_client = EventClient(logger)
    product_client = ProductClient(logger)

    return OrderService(
        create_use_case=CreateOrderUseCase(
            repository,
            user_client=user_client,
            event_client=event_client,
            product_client=product_client,
            ticket_client=ticket_client,
            logger=logger,
        ),
        get_use_case=GetOrderUseCase(repository),
        list_use_case=ListOrdersUseCase(repository),
        logger=logger,
        reservation_client=ReservationClient(logger),
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(
    payload: CreateOrderSchema, service: OrderService = Depends(get_service)
):
    # Validação de segurança – confere se total informado bate com a soma dos itens
    total_itens = sum(i.unit_price * i.quantity for i in payload.items)
    total_produtos = sum(p.unit_price * p.quantity for p in payload.products or [])
    total_calculado = round(total_itens + total_produtos, 2)

    if round(payload.total, 2) != total_calculado:
        raise HTTPException(
            status_code=400,
            detail=f"Total informado ({payload.total}) difere do calculado ({total_calculado})",
        )

    try:
        order = Order.from_schema(payload)
        return await service.create(order)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Erro ao criar pedido: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro ao criar pedido")


@router.get("/{order_id}", response_model=OrderResponseSchema)
def get_order(order_id: int, service: OrderService = Depends(get_service)):
    return service.get(order_id)


@router.get("/", response_model=List[OrderResponseSchema])
def list_orders(service: OrderService = Depends(get_service)):
    return service.list()
