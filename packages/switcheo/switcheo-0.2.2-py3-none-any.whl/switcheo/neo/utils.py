#
# switcheo/neo/utils.py
# Keith Smith
#
# For testnet requests to the Switcheo exchange

import math
import binascii
import base58
from neocore.Cryptography.Crypto import Crypto
from neocore.KeyPair import KeyPair
from neocore.Cryptography.Helper import scripthash_to_address
from switcheo.utils import stringify_message, reverse_hex
from switcheo.neo.transactions import serialize_transaction


def sign_message(encoded_message, private_key_hex):
    return Crypto.Sign(message=encoded_message.strip(), private_key=private_key_hex).hex()


def sign_transaction(transaction, private_key_hex):
    serialized_transaction = serialize_transaction(transaction=transaction, signed=False)
    return sign_message(encoded_message=serialized_transaction, private_key_hex=private_key_hex)


def sign_array(messages, private_key_hex):
    message_dict = {}
    for message in messages:
        message_dict[message['id']] = sign_transaction(transaction=message['txn'],
                                                       private_key_hex=private_key_hex)
    return message_dict


def encode_message(message):
    message_hex = binascii.hexlify(stringify_message(message).encode('utf-8')).decode()
    message_hex_length = hex(int(len(message_hex) / 2))[2:]
    return '010001f0' + message_hex_length + message_hex + '0000'


def to_neo_asset_amount(amount):
    if 0.00000001 < amount < 1000000:
        return "{:.0f}".format(amount * math.pow(10, 8))
    else:
        raise ValueError('Asset amount {} outside of acceptable range {}-{}.'.format(amount, 0.00000001, 1000000))


def private_key_to_hex(key_pair):
    return bytes(key_pair.PrivateKey).hex()


def neo_get_scripthash_from_address(address):
    """
    Convert a Public Address String to a ScriptHash (Address) String.

    :param address: The Public address to convert.
    :type address: str
    :return: String containing the converted ScriptHash.
    """
    hash_bytes = binascii.hexlify(base58.b58decode_check(address))
    return reverse_hex(hash_bytes[2:].decode('utf-8'))


def neo_get_address_from_scripthash(scripthash):
    """
    Core methods for manipulating keys
    NEP2 <=> WIF <=> Private => Public => ScriptHash <=> Address
    Keys are arranged in order of derivation.
    Arrows determine the direction.
    """
    scripthash_bytes = binascii.unhexlify(reverse_hex(scripthash))
    return scripthash_to_address(scripthash_bytes)


def neo_get_public_key_from_private_key(private_key):
    kp = KeyPair(priv_key=private_key)
    return kp.PublicKey


def neo_get_scripthash_from_private_key(private_key):
    script = b'21' + neo_get_public_key_from_private_key(private_key).encode_point(True) + b'ac'
    return Crypto.ToScriptHash(data=script)


def open_wallet(private_key):
    pk = bytes.fromhex(private_key)
    return KeyPair(priv_key=pk)
