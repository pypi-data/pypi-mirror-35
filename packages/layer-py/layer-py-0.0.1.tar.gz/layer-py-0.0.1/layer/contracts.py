import json
from web3 import Web3


LAYER_ADDRESS = '0xb22a7c73cc082a52471d12d9f0e013ae6d25c583'
LAYER_ABI = json.loads("[]")  # <abi-json-string>
DEFAULT_GETH_RPC_HOST = 'http://34.233.128.254:8555'


class Contracts:

    def __init__(self, geth_rpc_host=DEFAULT_GETH_RPC_HOST):
        w3 = Web3(Web3.HTTPProvider(geth_rpc_host))
        self.w3 = w3
        # self.layer_contract = w3.eth.contract(
        #     address=LAYER_ADDRESS, abi=LAYER_ABI)
        self.layer_contract = None

    def getBlockNumber(self):
        # it is test function
        return self.w3.eth.blockNumber

    def getLayernodes(self):
        return self.layer_contract.functions.getLayernodes([]).call()
        # layer_contract.functions.getLayernodes(params).call()

    def addLayernode(self, data):
        return self.layer_contract.functions.addLayernode([data]).call()

    def deleteLayernode(self, data):
        return self.layer_contract.functions.deleteLayernode([data]).call()

    def updateLayernode(self, data):
        return self.layer_contract.functions.updateLayernode([data]).call()

    def getProviers(self):
        return self.layer_contract.functions.getProviers([]).call()
