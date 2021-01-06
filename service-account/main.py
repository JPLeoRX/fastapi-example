from fastapi import FastAPI
from resource_ping import ping_router


app = FastAPI()


app.include_router(ping_router)