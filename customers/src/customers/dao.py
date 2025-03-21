from src.dao.base import BaseDAO
from src.customers.models import Customers


class CustomersDAO(BaseDAO):
    model = Customers
