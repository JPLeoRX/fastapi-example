from fastapi import APIRouter
from ping_output import PingOutput


ping_router = APIRouter()


@ping_router.get("/ping", response_model=PingOutput)
async def ping():
    return PingOutput('my-id', True)
