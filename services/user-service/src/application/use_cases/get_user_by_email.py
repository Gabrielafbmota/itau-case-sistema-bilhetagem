from src.domain.repositories.user_repository import IUserRepository


class GetUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, email: str):
        return self.user_repository.get_user_by_email(email)
