from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.domain.schemas.user_schema import UserCreate, UserResponse
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.use_cases.create_user import CreateUserUseCase
from src.application.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


def get_user_service(db: Session = Depends(DatabaseSession().get_session)):
    repo = UserRepository(db)
    use_case = CreateUserUseCase(repo)
    return UserService(use_case)


@router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate, service: UserService = Depends(get_user_service)
):
    return service.create(user_data)
