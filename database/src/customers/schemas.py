from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Customer(BaseModel):
    email: EmailStr
    password: str
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    phone: PhoneNumber
