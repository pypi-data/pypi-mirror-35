import json
from layer import common
from layer.signer import Signer
import requests

DEFAULT_LAYERNODE_ENDPOINT = 'http://54.146.96.85:7001'


class Layernode:
    """
    Layernode class
    """

    signer = None

    def __init__(self, api_endpoint=None, signer_endpoint=None):
        """
        Layernode constructor
        """
        self.signer = Signer(signer_endpoint)

    @staticmethod
    def verify_identity_signature(hash, address, keyHash, provider_sig, signer_sig):
        """identity_add verify in layernode"""
        # {
        #     'signer_request': {
        #         'provider_request': {
        #             'address': '0x011a28420578a06728dd537754d0f3d9b73e5f57',
        #             'keyHash': '1413f5327216dca7ed7b7f8632d2a203a0892aba',
        #             'hash': 'Hello World'
        #         },
        #         'provider_sig': '0xa2f74a9f636da1ccc37e193a27564939aeb9692694b69b4ddd6a21e964de6686417934225e06ecab3c4693b6364d2078e03f1989e52c595b079b66fcf7b10bdd1b'
        #     },
        #     'signer_sig': '3065023100fbe668f78bc6ef9ecf078d9aacf40617883a1d6dc079222d01cc1aa92f1c9e7542858fa2ad75253cbe1bc1476de181f5023079d92b41b2f0c3ec4a4fef96bb33b06b4b75040e45851716ec531d625c17d536dcee1f79aab28e109f385b867dfc520d'
        # }

        # make data structure
        provider_request = {'hash': hash,
                            'address': address, 'keyHash': keyHash}
        signer_request = {
            'provider_request': provider_request,
            'provider_sig': provider_sig
        }

        # signer verify
        # skip for now, will come later
        # return 2

        # provider verify
        if not common.web3_verify(provider_request, provider_sig, address):
            # provider_sig is not verified
            return 1

        return 0

    @staticmethod
    def verify_score_signature(hash, address, keyHash, score, category, provider_sig, signer_sig):
        """score_add verify in layernode"""
        # {
        #     'signer_request': {
        #         'provider_request': {
        #             'address': '0x011a28420578a06728dd537754d0f3d9b73e5f57',
        #             'keyHash': '1413f5327216dca7ed7b7f8632d2a203a0892aba',
        #             'hash': 'Hello World'
        #             "score":2,
        #             "category":"ProviderTransactionCategory"
        #         },
        #         'provider_sig': '0xa2f74a9f636da1ccc37e193a27564939aeb9692694b69b4ddd6a21e964de6686417934225e06ecab3c4693b6364d2078e03f1989e52c595b079b66fcf7b10bdd1b'
        #     },
        #     'signer_sig': '3065023100fbe668f78bc6ef9ecf078d9aacf40617883a1d6dc079222d01cc1aa92f1c9e7542858fa2ad75253cbe1bc1476de181f5023079d92b41b2f0c3ec4a4fef96bb33b06b4b75040e45851716ec531d625c17d536dcee1f79aab28e109f385b867dfc520d'
        # }

        # make data structure
        provider_request = {'hash': hash, 'address': address,
                            'keyHash': keyHash, 'score': score, 'category': category}
        signer_request = {
            'provider_request': provider_request,
            'provider_sig': provider_sig
        }

        # signer verify
        # skip for now, will come later
        # return 2

        # provider verify
        if not common.web3_verify(provider_request, provider_sig, address):
            # provider_sig is not verified
            return 1

        return 0

    @staticmethod
    def verify_provider_signature(provider_request, provider_sig, address):
        """verify provider signature"""

        # provider verify
        if not common.web3_verify(provider_request, provider_sig, address):
            # provider_sig is not verified
            return 1

        return 0
