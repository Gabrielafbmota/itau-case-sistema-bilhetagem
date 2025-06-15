from pydantic import BaseModel, EmailStr

class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
