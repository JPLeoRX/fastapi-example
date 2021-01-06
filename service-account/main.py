from injectable import load_injection_container
from fastapi import FastAPI
from resource_ping import router_ping
from resource_account import router_account


load_injection_container()
app = FastAPI()
app.include_router(router_ping)
app.include_router(router_account)
