from logging import Logger
from fastapi import HTTPException
from typing import Optional
from src.application.use_cases.create_user import CreateUserUseCase
from src.application.use_cases.get_user_by_email import GetUserUseCase
from src.application.use_cases.get_user_by_id import GetUserByIdUseCase

from src.domain.schemas.user_schema import UserCreate, UserResponse


class UserService:

    def __init__(
        self,
        create_user_use_case: CreateUserUseCase,
        get_user_use_case: GetUserUseCase,
        get_user_by_id_use_case: GetUserByIdUseCase,
        logger: Logger,
    ) -> None:
        self.create_user_use_case = create_user_use_case
        self.get_user_use_case = get_user_use_case
        self.get_user_by_id_use_case = get_user_by_id_use_case
        self.logger = logger

    def create(self, user_data: UserCreate) -> UserResponse:

        user = self.get_user_use_case.execute(user_data.email)
        self.logger.info(f"User found: {user}")

        if not user:
            user = self.create_user_use_case.execute(user_data)
        return user

    def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        user = self.get_user_use_case.execute(email)
        if not user:
            return None
        return user

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.get_user_by_id_use_case.execute(user_id)
        if not user:
            raise HTTPException(404, detail="User not found")
        return user
