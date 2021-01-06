class AccountModel:
    def __init__(self, id: str, username: str, password: str, image_url: str, registration_timestamp: int) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.image_url = image_url
        self.registration_timestamp = registration_timestamp
