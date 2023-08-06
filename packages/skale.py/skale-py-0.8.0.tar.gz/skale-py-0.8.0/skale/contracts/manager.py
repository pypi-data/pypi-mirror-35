from web3 import Web3
import socket
import logging

from skale.contracts import BaseContract
import skale.utils.helper as Helper
from skale.utils.helper import format

from skale.utils.constants import NODE_DEPOSIT, GAS, OP_TYPES

logger = logging.getLogger(__name__)


class Manager(BaseContract):

    def create_node(self, ip, port, wallet):
        logger.info(f'create_node: {ip}:{port}')

        token = self.skale.get_contract_by_name('token')

        skale_nonce = Helper.generate_nonce()
        transaction_data = self.create_node_data_to_bytes(ip, port, wallet['address'], skale_nonce)

        eth_nonce = self.skale.web3.eth.getTransactionCount(wallet['address'])
        op = token.contract.functions.transfer(self.address, NODE_DEPOSIT, transaction_data)
        create_node_txn = op.buildTransaction({
            'gas': GAS['create_node'],
            'nonce': eth_nonce
        })

        self.skale.web3.eth.enable_unaudited_features()  # todo: deal with this!
        signed_txn = self.skale.web3.eth.account.signTransaction(create_node_txn, private_key=wallet['private_key'])

        tx = self.skale.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        logger.info(f'create_node transaction_hash: {self.skale.web3.toHex(tx)}')
        return {'tx': tx, 'nonce': skale_nonce}

    def create_node_data_to_bytes(self, ip, port, address, nonce):
        address_fx = Web3.toChecksumAddress(address)[2:]  # cut 0x

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

    def get_node_next_reward_date(self, node_index):
        return self.contract.functions.getNodeNextRewardDate(node_index).call()