from fastapi import APIRouter, Depends

from src.customers.schemas import Customer, CustomerLogin, CustomerResponse
from src.customers.dao import CustomersDAO
from src.customers.dependencies import get_current_user

from src.auth.auth import get_password_hash, authenticate_customer, create_access_token
from src.exceptions import UserAlreadyExistsException
from src.customers.produser import send_message


customers_router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)


@customers_router.get("", response_model=CustomerResponse)
async def get_customers(current_customer=Depends(get_current_user)):
    return current_customer


@customers_router.post("/register", status_code=201)
async def register(customer_data: Customer):
    existing_customer = await CustomersDAO.find_one_or_none(email=customer_data.email)
    if existing_customer:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(customer_data.password)
    customer_data.password = hashed_password
    await send_message(customer_data.model_dump_json())
    return {"details": f"Customer {customer_data.email} was created"}


@customers_router.post("/login")
async def login(customer_data: CustomerLogin):
    customer = await authenticate_customer(customer_data.email, customer_data.password)
    access_token = create_access_token({"sub": str(customer.uuid)})
    return {"access_token": access_token}


@customers_router.post("/logout")
async def logout():
    return {"message": "Hello World"}
