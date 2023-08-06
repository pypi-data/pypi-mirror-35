from .blockchain_utils import *
from .ipfs_utils import *
from eth_utils import is_address, to_checksum_address
from solc import compile_source, compile_files

abi = '''[{"constant":true,"inputs":[{"name":"id","type":"uint256"}],"name":"getter","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"id","type":"uint256"},{"name":"value","type":"string"}],"name":"setter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"metaDb","outputs":[{"name":"value","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'''

class Client(object):
	def __init__(self):
		print('1')
		self.web3 = Web3(HTTPProvider('http://54.153.84.146:8545'))
		print('2')
		assert self.web3.isConnected()
		print('3')
		# self.api = ipfsapi.connect('127.0.0.1', 5001)
		print('4')
		contract_path= 'Database.sol'
		MY_ADDRESS = '0xf6419f5c5295a70C702aC21aF0f64Be07B59F3c4'
		CONTRACT_ADDRESS = to_checksum_address('0x2d3dbaa17e79c9ad964c88d2351d6157648de148')
		CLIENT_ADDRESS = '0x62Bf957bC69721BEbfB82b8A09D6123dCC372DFc'
		self.web3.personal.unlockAccount(MY_ADDRESS, 'panda')
		# compiled_sol = compile_files('Database.sol')
		# Database_id, Database_interface = compiled_sol.popitem()
		self.contract_obj = self.web3.eth.contract(address=CONTRACT_ADDRESS,
				   abi=abi)
		self.clientAddress = MY_ADDRESS

	def setter(self, key, value):
		tx_hash = self.contract_obj.functions.setter(key, value).transact({'from': self.clientAddress})
		self.web3.eth.waitForTransactionReceipt(tx_hash)
		tx_receipt = self.web3.eth.getTransactionReceipt(tx_hash)
		return tx_receipt

	def getter(self, key):
		tx_hash = self.contract_obj.functions.getter(key).transact({'from': self.clientAddress})
		self.web3.eth.waitForTransactionReceipt(tx_hash)
		tx_receipt = self.web3.eth.getTransactionReceipt(tx_hash)
		return tx_receipt