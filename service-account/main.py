from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PingOutput(BaseModel):
    id: str
    success: bool

    def __init__(self, id: str, success: bool) -> None:
        super().__init__(id=id, success=success)


@app.get("/ping", response_model=PingOutput)
def ping():
    return PingOutput('hello', True)
