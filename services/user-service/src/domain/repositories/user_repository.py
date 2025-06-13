from abc import ABC, abstractmethod
from src.domain.schemas.user_schema import UserCreate
from src.infrastructure.database.models.user_model import UserModel


class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user_data: UserCreate) -> UserModel: ...
