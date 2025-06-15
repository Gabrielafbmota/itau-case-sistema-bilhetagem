from src.infrastructure.repositories.user_repository import UserRepository
from src.core.security import verify_password
from src.domain.entities.user import UserEntity


class LoginUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> UserEntity | None:
        user = self.user_repository.get_user_by_email(email)
        if not user or not verify_password(password, str(user.hashed_password)):
            return None
        return user
