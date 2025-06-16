from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    user_id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
