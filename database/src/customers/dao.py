from dao.base import BaseDAO
from customers.models import Customers


class CustomersDAO(BaseDAO):
    model = Customers
