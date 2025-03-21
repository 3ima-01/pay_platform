from fastapi import Depends, Request

from jose import JWTError, jwt

from src.customers.dao import CustomersDAO
from src.config import settings
from src.exceptions import (
    IncorrectTokenFormatException,
    UserIsNotPresentException,
    TokenNotFoundException,
)


def get_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise TokenNotFoundException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectTokenFormatException
    customer_uuid: str = payload.get("sub")
    if not customer_uuid:
        raise UserIsNotPresentException
    user = await CustomersDAO.find_one_or_none(uuid=customer_uuid)
    if not user:
        raise UserIsNotPresentException

    return user
