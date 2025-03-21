from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Parners(Base):
    __tablename__ = "partners"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class Payments(Base):
    __tablename__ = "payments"
    id: Mapped[str] = mapped_column(primary_key=True)
    customer_id: Mapped[str]
    created_at: Mapped[str]
    paymentType: Mapped[str]
    state: Mapped[str]
    amount: Mapped[float]
    currency: Mapped[str]
    customerAmount: Mapped[float]
    customerCurrency: Mapped[str]
    externalResultCode: Mapped[str]
    terminalName: Mapped[str]

    {
        "id": "0a0eb99661f24b7287e1a30a2e9a7c94",
        "created": "2025-03-21T09:21:21.040612255",
        "paymentType": "WITHDRAWAL",
        "state": "COMPLETED",
        "internalState": "COMPLETED",
        "paymentMethod": "BASIC_CARD",
        "paymentMethodDetails": {
            "customerAccountNumber": "214354***0897",
            "cardholderName": "adawdwa adaw",
            "cardExpiryMonth": "02",
            "cardExpiryYear": "2053",
        },
        "amount": 12.12,
        "currency": "EUR",
        "customerAmount": 12.12,
        "customerCurrency": "EUR",
        "externalResultCode": "0",
        "externalRefs": {
            "withdrawTransactionGuid": "f8d4ad8b-837e-4ef4-8a51-5f6bef2b96ee",
            "withdrawTransactionId": "909",
        },
        "customer": {"locale": "ru_RU"},
        "terminalName": "Payvision Emulator SANDBOX",
    }
