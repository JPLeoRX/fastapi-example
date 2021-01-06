from fastapi import APIRouter

from account_output import AccountOutput
from ping_output import PingOutput
from service_account import ServiceAccount

router_account = APIRouter()
service_account = ServiceAccount()


@router_account.get("/account/get", response_model=AccountOutput)
def get(id: str):
    account = service_account.get(id)
    return AccountOutput(account.id, account.username, account.image_url, account.registration_timestamp)
