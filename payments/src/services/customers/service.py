import json
import httpx
from src.config import settings

from src.payments.produser import send_message


class CustomersService:

    def __init__(self):
        self.API_URL = settings.CUSTOMERS_URL

    async def verify_token(self, token: str):
        url = f"{self.API_URL}/validate"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers={"Authentication": f"{token}"})
            return response.json()
