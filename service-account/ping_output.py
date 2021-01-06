from pydantic import BaseModel


class PingOutput(BaseModel):
    id: str
    success: bool

    def __init__(self, id: str, success: bool) -> None:
        super().__init__(id=id, success=success)
