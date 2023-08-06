from skale.contracts import BaseContract
from skale.utils.helper import format

class SChains(BaseContract):
    fields = [
        'owner',
        'name',
        'storageBytes',
        'cpu',
        'transactionThroughput',
        'lifetime',
        'creationDate',
        'maxNodes',
        'deposit'
    ]

    def __get_raw(self, name):
        return self.contract.functions.getSchain(name).call()

    @format(fields)
    def get(self, name):
        return self.__get_raw(name)
