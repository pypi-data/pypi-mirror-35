from web3 import Web3
import socket
import logging

from skale.contracts import BaseContract
import skale.utils.helper as Helper
from skale.utils.constants import NODE_DEPOSIT, GAS, OP_TYPES

logger = logging.getLogger(__name__)


class NodeManager(BaseContract):

    def create_node(self, ip, port, wallet):
        logger.info(f'create_node: {ip}:{port}')

        token = self.skale.get_contract_by_name('token')
        transaction_data = self.create_node_data_to_bytes(ip, port, wallet['address'])

        nonce = self.skale.web3.eth.getTransactionCount(wallet['address'])
        op = token.contract.functions.transfer(self.address, NODE_DEPOSIT, transaction_data)
        create_node_txn = op.buildTransaction({
            'gas': GAS['create_node'],
            'nonce': nonce
        })

        self.skale.web3.eth.enable_unaudited_features()  # todo: deal with this!
        signed_txn = self.skale.web3.eth.account.signTransaction(create_node_txn, private_key=wallet['private_key'])

        tx = self.skale.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        logger.info(f'create_node transaction_hash: {self.skale.web3.toHex(tx)}')
        return {'tx': tx, 'nonce': nonce}

    def create_node_data_to_bytes(self, ip, port, address):
        address_fx = Web3.toChecksumAddress(address)[2:]  # cut 0x
        nonce = Helper.generate_nonce()

        type_bytes = OP_TYPES['create_node'].to_bytes(1, byteorder='big')
        port_bytes = port.to_bytes(4, byteorder='big')
        nonce_bytes = nonce.to_bytes(4, byteorder='big')  # todo
        ip_bytes = socket.inet_aton(ip)
        address_bytes = bytes.fromhex(address_fx)

        data_bytes = type_bytes + port_bytes + nonce_bytes + ip_bytes + address_bytes
        logger.info(f'create_node_data_to_bytes bytes: {self.skale.web3.toHex(data_bytes)}')

        return data_bytes

    def get_bounty(self, node_id, account):
        transaction_opts = {
            'from': account,
            'gas': GAS['get_bounty']
        }
        return self.contract.functions.getBounty(node_id).transact(transaction_opts)

    def send_verdict(self, validator, node_id, downtime, latency, account):
        transaction_opts = {
            'from': account,
            'gas': GAS['send_verdict']
        }
        return self.contract.functions.sendVerdict(validator, node_id, downtime, latency).transact(transaction_opts)

    def get_validated_array(self, node_id, account):
        return self.contract.functions.getValidatedArray(node_id).call({'from': account})

    def __get_node_raw(self, node_id):
        return self.contract.functions.getNode(node_id).call()

    def get_node(self, node_id):
        node_arr = self.__get_node_raw(node_id)
        return self.node_arr_to_obj(node_arr)

    def node_arr_to_obj(self, node_arr):
        return {
            'ip': socket.inet_ntoa(node_arr[0]),
            'port': node_arr[1],
            # 'status': node_arr[2],
            'public_key': node_arr[2],
            'last_reward_date': node_arr[3],
            'leaving_date': node_arr[4],
            'start_date': node_arr[5]
        }

    def get_active_node_ids(self):
        return self.contract.functions.getActiveNodeIds().call()
