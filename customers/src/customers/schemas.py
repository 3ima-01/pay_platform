from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Customer(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    phone: PhoneNumber = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "stringst",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "+375256666666",
            }
        }


class CustomerResponse(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: PhoneNumber


class CustomerLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)
