from injectable import injectable
from account_model import AccountModel


@injectable
class ServiceAccount:
    def get(self, id: str) -> AccountModel:
        return AccountModel(id, 'my-username', 'my-password', 'my-image', -1)
