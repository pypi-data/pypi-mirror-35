import requests
import json
from web3 import Web3
from eth_account.messages import defunct_hash_message

w3 = Web3()


def web3_sign(msg, private_key):
    """Message sign function with current private key
    Args:
        msg (str): A message to sign
    Returns:
        str: The signature.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    message_hash = defunct_hash_message(text=msg)
    signed_message = w3.eth.account.signHash(
        message_hash, private_key=private_key
    )
    str_sign = '0x' + ''.join('{:02x}'.format(x)
                              for x in signed_message.signature)
    return str_sign


def web3_recover_address(msg, signature):
    """Recover address from message and signature
    Args:
        msg (str): A message to recover
        signature (str): A signature to generated with
                            private key and above message
    Returns:
        str: The recovered address.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    message_hash = defunct_hash_message(text=msg)
    address = w3.eth.account.recoverHash(message_hash, signature=signature)
    return address


def web3_verify(msg, signature, address):
    """Verify message and siganture using private key
    Args:
        msg (str): A message to verify
        signature (str): A signature to verify
    Returns:
        bool: True if successfully verify the message, False otherwise.
    """
    if isinstance(msg, dict):
        msg = json.dumps(msg, sort_keys=True)

    _address = web3_recover_address(msg, signature)
    return _address.lower() == address.lower()
