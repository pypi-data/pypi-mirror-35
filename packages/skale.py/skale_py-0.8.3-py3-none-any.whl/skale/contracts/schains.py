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

    def get_schain_nodes(self, schain_name):
        return self.contract.functions.getSchainNodes(schain_name).call()

    def get_schain_list_size(self, account):
        return self.contract.functions.getSchainListSize().call({'from': account})

    def get_schain_by_index(self, index):
        return self.contract.functions.getSchainByIndex(index).call()

    def get_schain_name_by_schain_id(self, schain_id):
        return self.contract.functions.getSchainNameBySchainId(schain_id).call()

    def get_schain_ids_for_node(self, node_id):
        return self.contract.functions.getSchainIdsForNode(node_id).call()

    def get_schains_for_node(self, node_id):
        schains = []
        schain_contract = self.skale.get_contract_by_name('schains')
        schain_ids = self.get_schain_ids_for_node(node_id)
        for schain_id in schain_ids:
            name = self.get_schain_name_by_schain_id(schain_id)
            schain = schain_contract.get(name)
            schains.append(schain)
        return schains
