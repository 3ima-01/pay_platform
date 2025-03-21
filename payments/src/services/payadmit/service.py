import json
import httpx
from src.config import settings

from src.payments.produser import send_message


class PayAdmitService:

    def __init__(self):
        self.API_URL = settings.PAYADMIT_URL
        self.API_KEY = settings.PAYADMIT_KEY
        self.HEADERS = {"Authorization": f"Bearer {self.API_KEY}"}

    async def get_payments(self):
        url = f"{self.API_URL}/payments"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.HEADERS)
            return response.json()

    async def deposite(self, body, user_uuid):
        url = f"{self.API_URL}/payments"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, headers=self.HEADERS, json=json.loads(body)
            )
            result = response.json()["result"]
            result["user_uuid"] = user_uuid
            send_message(result)

    async def withdrawal(self, body, user_uuid):
        url = f"{self.API_URL}/payments"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, headers=self.HEADERS, json=json.loads(body)
            )
            result = response.json()["result"]
            result["user_uuid"] = user_uuid
            send_message(result)

    async def refund(self, body, user_uuid):
        url = f"{self.API_URL}/payments"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, headers=self.HEADERS, json=json.loads(body)
            )
            result = response.json()
            result["user_uuid"] = user_uuid
            send_message(result)

    async def confirm_payout(self, body):
        url = f"{self.API_URL}/payments/confirmPayout"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, headers=self.HEADERS, json=json.loads(body)
            )
            return response.json()

    async def check_status(self, payment_id: str):
        url = f"{self.API_URL}/payments/{payment_id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.HEADERS)
            return response.json()

    async def get_operations(self, payment_id: str):
        url = f"{self.API_URL}/payments/{payment_id}/operations"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.HEADERS)
            return response.json()

    async def get_balance(self, terminalId: int, currency: str):

        url = f"{self.API_URL}/terminals/getBalance/{terminalId}"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url, headers=self.HEADERS, params={"currency": currency}
            )
            return response.json()

    async def update_whitelist(self, body):
        url = f"{self.API_URL}/updateWhitelist"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, headers=self.HEADERS, json=json.loads(body)
            )
            return response.json()

    async def update_blacklist(self, body):
        url = f"{self.API_URL}/updateBlacklist"
        async with httpx.AsyncClient() as client:
            print([json.loads(body)])
            response = await client.post(
                url, headers=self.HEADERS, json=[json.loads(body)]
            )
            return response.json()
