from fastapi import APIRouter, Depends
from src.services.payadmit.service import PayAdmitService

from src.payments.dependencies import validate_token

from src.payments.schemas import (
    Deposite,
    Withdrawal,
    Refund,
    Confirm,
    BlackList,
)
from src.services.payadmit.enums import Currency

payadmit = PayAdmitService()

payments_router = APIRouter(prefix="/payments", tags=["Payments"])


@payments_router.get("/")
async def get_payments():
    return await payadmit.get_payments()


@payments_router.post("/deposite")
async def create_deposite(deposite_data: Deposite, user_uuid=Depends(validate_token)):
    return await payadmit.deposite(deposite_data.model_dump_json(), user_uuid)


@payments_router.post("/withdrawal")
async def create_withdrawal(
    withdrawal_data: Withdrawal, user_uuid=Depends(validate_token)
):
    return await payadmit.withdrawal(withdrawal_data.model_dump_json(), user_uuid)


@payments_router.post("/refund")
async def create_refund(refund_data: Refund, user_uuid=Depends(validate_token)):
    return await payadmit.refund(refund_data.model_dump_json(), user_uuid)


@payments_router.post("/confirm_payout")
async def confirm_payout(confirm_data: Confirm):
    return await payadmit.confirm_payout(confirm_data.model_dump_json())


@payments_router.post("/update_whitelist")
async def update_whitelist():
    return await payadmit.update_whitelist()


@payments_router.post("/update_blacklist")
async def update_blacklist(blacklist_data: BlackList):
    return await payadmit.update_blacklist(
        blacklist_data.model_dump_json(exclude_none=True)
    )


@payments_router.get("/check_status/{payment_id}")
async def check_status(payment_id: str):
    return await payadmit.check_status(payment_id)


@payments_router.get("/get_operations/{payment_id}")
async def get_operations(payment_id: str):
    return await payadmit.get_operations(payment_id)


@payments_router.get("/get_balance/{terminalId}")
async def get_balance(terminalId: int, currency: Currency):
    return await payadmit.get_balance(terminalId, currency.value)
