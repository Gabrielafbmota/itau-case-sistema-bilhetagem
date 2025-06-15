from pydantic import BaseModel, EmailStr, Field

class UserRegisterInput(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserLoginInput(BaseModel):
    email: EmailStr
    password: str
