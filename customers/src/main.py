from fastapi import FastAPI

from src.config import settings

from src.auth.routers import auth_router
from src.customers.routers import customers_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(auth_router)
app.include_router(customers_router)
