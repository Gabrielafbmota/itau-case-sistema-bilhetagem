from src.application.use_cases.create_user import CreateUserUseCase
from src.application.use_cases.get_user_by_email import GetUserUseCase
from src.application.use_cases.get_user_by_id import GetUserByIdUseCase
from src.application.use_cases.login_user import LoginUserUseCase
from src.domain.schemas.user_schema import UserCreate, UserResponse
from src.core.logger import get_logger
from src.domain.entities.user import UserEntity


class UserService:
    def __init__(
        self,
        create_user_use_case: CreateUserUseCase | None = None,
        get_user_by_id_use_case: GetUserByIdUseCase | None = None,
        login_use_case: LoginUserUseCase | None = None,
        get_user_by_email_use_case: GetUserUseCase | None = None,
        logger=get_logger(),
    ):
        self.create_user_use_case = create_user_use_case
        self.get_user_by_id_use_case = get_user_by_id_use_case
        self.login_use_case = login_use_case
        self.get_user_by_email_use_case = get_user_by_email_use_case
        self.logger = logger

    def create(self, user_data: UserCreate) -> UserResponse:
        if not self.create_user_use_case:
            raise ValueError("Create user use case not initialized")
        return self.create_user_use_case.execute(user_data)

    def get_user_by_id(self, user_id: int) -> UserResponse:
        if not self.get_user_by_id_use_case:
            raise ValueError("Get user by id use case not initialized")
        return self.get_user_by_id_use_case.execute(user_id)

    def login(self, email: str, password: str) -> UserEntity | None:
        if not self.login_use_case:
            raise ValueError("Login use case not initialized")
        return self.login_use_case.execute(email, password)

    def get_user_by_email(self, email: str) -> UserResponse | None:
        if not self.get_user_by_email_use_case:
            raise ValueError("Get user by email use case not initialized")
        return self.get_user_by_email_use_case.execute(email)
