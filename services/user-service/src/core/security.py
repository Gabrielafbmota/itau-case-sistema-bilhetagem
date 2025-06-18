from passlib.hash import bcrypt
import jwt
import time

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
def hash_password(password: str) -> str:
    return bcrypt.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.verify(plain, hashed)


def create_access_token(data: dict, expires_delta) -> str:
    """Gera token JWT com tempo de expiração."""

    to_encode = data.copy()
    if expires_delta:
        expire = time.time() + expires_delta.total_seconds()
        to_encode.update({"expires": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> dict | None:
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
