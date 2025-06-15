from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False


class Token(BaseModel):
    access_token: str
    token_type: str
