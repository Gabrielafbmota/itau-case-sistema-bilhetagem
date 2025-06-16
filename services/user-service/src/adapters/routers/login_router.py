from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.user_repository import UserRepository
from src.application.use_cases.login_user import LoginUserUseCase
from src.application.use_cases.get_user_by_email import (
    GetUserUseCase as GetUserByEmailUseCase,
)
from src.application.services.user_service import UserService
from src.domain.schemas.user_schema import Token, User
from src.core.security import create_access_token, decode_access_token
from src.core.logger import get_logger

auth_router = APIRouter(tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

logger = get_logger()


def get_user_service(db: Session = Depends(DatabaseSession().get_session)):
    repo = UserRepository(db)
    login_use_case = LoginUserUseCase(repo)
    get_user_by_email_use_case = GetUserByEmailUseCase(repo)
    return UserService(
        login_use_case=login_use_case,
        get_user_by_email_use_case=get_user_by_email_use_case,
        logger=logger,
    )


@auth_router.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service),
):
    user = service.login(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/users/me", response_model=User)
def read_users_me(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(get_user_service),
):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    user = service.get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user
