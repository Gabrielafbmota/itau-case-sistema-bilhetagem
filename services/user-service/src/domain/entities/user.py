from dataclasses import dataclass
from typing import Optional


@dataclass
class UserEntity:
    id: int
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False
    hashed_password: Optional[str] = None
