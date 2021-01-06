from fastapi import APIRouter
from ping_output import PingOutput


router_ping = APIRouter()


@router_ping.get("/ping", response_model=PingOutput)
async def ping():
    return PingOutput('my-id', True)
