from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from pydantic import EmailStr

from src.customers.dao import CustomersDAO
from src.config import settings

from src.exceptions import IncorrectEmailOrPasswordException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


async def authenticate_customer(email: EmailStr, password: str):
    customer = await CustomersDAO.find_one_or_none(email=email)
    if not (customer and verify_password(password, customer.password)):
        raise IncorrectEmailOrPasswordException
    return customer
