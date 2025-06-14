from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.domain.schemas.user_schema import UserCreate, UserResponse
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.use_cases.create_user import CreateUserUseCase
from src.application.use_cases.get_user_by_email import GetUserUseCase
from src.application.use_cases.get_user_by_id import GetUserByIdUseCase
from src.application.services.user_service import UserService
from src.core.logger import get_logger

user_router = APIRouter(prefix="/users", tags=["Users"])

logger = get_logger()

def get_user_service(db: Session = Depends(DatabaseSession().get_session)):
    repo = UserRepository(db)
    use_case = CreateUserUseCase(repo)
    get_user_use_case = GetUserUseCase(repo)
    get_user_by_id_use_case = GetUserByIdUseCase(repo)

    return UserService(use_case, get_user_use_case, get_user_by_id_use_case, logger)


@user_router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate, service: UserService = Depends(get_user_service)
):
    return service.create(user_data)


@user_router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    try:
        return service.get_user_by_id(user_id)
    except HTTPException as e:
        raise e
