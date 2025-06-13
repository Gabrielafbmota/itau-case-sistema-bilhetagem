from src.application.use_cases.create_user import CreateUserUseCase
from src.domain.schemas.user_schema import UserCreate, UserResponse


class UserService:
    def __init__(self, create_user_use_case: CreateUserUseCase):
        self.create_user_use_case = create_user_use_case

    def create(self, user_data: UserCreate) -> UserResponse:
        return self.create_user_use_case.execute(user_data)
