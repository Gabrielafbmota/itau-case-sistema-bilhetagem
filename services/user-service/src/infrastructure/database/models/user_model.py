from sqlalchemy import Column, Integer, String, DateTime, func
from src.infrastructure.database.session import Base

class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "bilheteria_schema"}

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email='{self.email}')>"
