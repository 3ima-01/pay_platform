from pydantic import BaseModel, Field
from src.services.payadmit.enums import PaymentType, PaymentMethod, Currency, Action

from typing import Optional


class Deposite(BaseModel):
    paymentType: PaymentType = PaymentType.DEPOSIT
    paymentMethod: PaymentMethod
    amount: float = Field(gt=0)
    currency: Currency


class Withdrawal(BaseModel):
    paymentType: PaymentType = PaymentType.WITHDRAWAL
    paymentMethod: PaymentMethod
    amount: float = Field(gt=0)
    currency: Currency


class Refund(BaseModel):
    paymentType: PaymentType = PaymentType.REFUND
    amount: float = Field(gt=0)
    currency: Currency
    parentPaymentId: str = Field(max_length=32)


class Confirm(BaseModel):
    paymentId: str = Field(max_length=32)
    action: Action


class BlackList(BaseModel):
    merchantId: int
    cardMask: Optional[str] = Field(default=None)
    customerEmail: Optional[str] = Field(default=None)
    customerPhone: Optional[str] = Field(default=None)
