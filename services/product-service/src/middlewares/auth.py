from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from src.domain.schemas.user_schema import User
import requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8000/token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        response = requests.get(
            "http://localhost:8000/users/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        response.raise_for_status()
        return User(**response.json())
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou usuário não autenticado",
        )


def get_current_admin_user(user: User = Depends(get_current_user)) -> User:
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado. Apenas administradores.",
        )
    return user
