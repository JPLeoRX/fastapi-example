from injectable import injectable, autowired, Autowired
from account_model import AccountModel
from utils_id import UtilsId


@injectable
class ServiceAccount:
    @autowired
    def __init__(self, utils_id: Autowired(UtilsId)):
        self.utils_id = utils_id

    def get(self, id: str) -> AccountModel:
        print(self.utils_id.generate_uuid())
        return AccountModel(id, 'my-username', 'my-password', 'my-image', -1)
