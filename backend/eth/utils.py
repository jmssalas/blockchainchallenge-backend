import hashlib

from eth import settings
from eth_account import Account


def sendTransaction(transaction, address, privateKey):
    transaction = transaction.buildTransaction()
    transaction['nonce'] = settings.W3.eth.getTransactionCount(address)
    transaction['chainId'] = 4
    signed = settings.W3.eth.account.signTransaction(transaction, privateKey)
    txn_hash = settings.W3.eth.sendRawTransaction(signed.rawTransaction)
    settings.W3.eth.waitForTransactionReceipt(txn_hash)

def sendTrack(data):
    print('data: ' + data)
    return sendTransaction(
        settings.TRACK_CONTRACT.functions.saveTrack(data),
        settings.ADMIN_ADDRESS,
        settings.ADMIN_PRIVATE_KEY
    )


def sendPoints(address, amount):
    return sendTransaction(
        settings.CIRCLE_TOKEN_CONTRACT.functions.transfer(address, amount),
        settings.ADMIN_ADDRESS,
        settings.ADMIN_PRIVATE_KEY
    )
