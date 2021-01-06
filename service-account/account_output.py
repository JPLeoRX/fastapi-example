from pydantic import BaseModel


class AccountOutput(BaseModel):
    id: str
    username: str
    image_url: str
    registration_timestamp: int

    def __init__(self, id: str, username: str, image_url: str, registration_timestamp: int) -> None:
        super().__init__(id=id, username=username, image_url=image_url, registration_timestamp=registration_timestamp)
