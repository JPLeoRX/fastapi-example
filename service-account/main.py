from fastapi import FastAPI
from ping_output import PingOutput


app = FastAPI()


@app.get("/ping", response_model=PingOutput)
def ping():
    return PingOutput('hello', True)
