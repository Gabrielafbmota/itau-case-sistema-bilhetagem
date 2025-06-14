from sqlalchemy.orm import Session
from src.domain.schemas.user_schema import UserCreate
from src.infrastructure.database.models.user_model import UserModel
from src.domain.repositories.user_repository import IUserRepository
from passlib.hash import bcrypt


class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate) -> UserModel:
        hashed_pw = bcrypt.hash(user_data.password)
        user = UserModel(
            name=user_data.name, email=user_data.email, hashed_password=hashed_pw
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.email == email).first()

    def get_user_by_id(self, user_id: int) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
