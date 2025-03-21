from fastapi import FastAPI
from src.payments.routers import payments_router

app = FastAPI(title="AmPay | Payments")

app.include_router(payments_router)
