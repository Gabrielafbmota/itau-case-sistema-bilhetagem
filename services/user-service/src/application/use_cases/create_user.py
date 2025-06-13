from src.domain.schemas.user_schema import UserCreate, UserResponse
from src.domain.repositories.user_repository import IUserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, user_data: UserCreate) -> UserResponse:
        user = self.user_repository.create_user(user_data)
        return UserResponse.from_orm(user)
