from hashlib import algorithms_available
import os

from datetime import datetime, timedelta
from typing import Union,Any

from jose import jwt
from passlib.context import CryptContext

from dotenv import load_dotenv
from pydantic import BaseSettings, HttpUrl

load_dotenv()

BASE_DIR: str = os.path.abspath(os.curdir)


class Settings(BaseSettings):
    SECRET_KEY: str = os.urandom(12).hex()
    SQLALCHEMY_DATABASE_URI: str = f'sqlite:///{BASE_DIR}/database.db'

    PROJECT_NAME: str = "Felipe_Blog"
    PROJECT_VERSION: str = "v0.0.2"
    API_V1_STR: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 3
    ALGORITHM: str = "HS256"
    BACKEND_CORS_ORIGINS: list[HttpUrl] = []

settings = Settings()

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_access_token(
    subject: Union[str,Any], expires_delta: timedelta = None
) -> str:
    """
    Crea el JWT con un subject y la hora actual 
    sumandole un tiempo por defecto o como parametro
    ----------
    PARAMETROS:
    - subject           el sujeto que solicita la creación del jwt.

    - expires_delta:    tiempo en el que expira el token, si no es pasado
                        se tomará el tiempo de expiración del settings, si 
                        es pasado como parametro, se tomará este
    -------
    RETURN:
    - token          tiempo en el que expira + subject.   
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta (
            minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp":expire,"sub":str(subject)}
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm = settings.ALGORITHM
    )


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> str:
    return password_context.verify(plain_password,hashed_password)


def get_password(
    password: str 
) -> str:
    return password_context.hash(password)