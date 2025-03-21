from fastapi import Depends, Request
from src.services.customers.service import CustomersService

customers_service = CustomersService()


def get_token(request: Request):
    token = request.headers.get("Authentication")
    if not token:
        return
    return token


async def validate_token(token: str = Depends(get_token)):
    return await customers_service.verify_token(token)
