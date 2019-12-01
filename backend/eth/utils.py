import hashlib

from eth import settings
from eth_account import Account


def sendTransaction(transaction, privateKey):
    account = Account()
    return transaction.call({'from': account.privateKeyToAccount(privateKey).address})


def sendTrack(data):
    return sendTransaction(settings.TRACK_CONTRACT.functions.saveTrack(hashlib.sha256(str(data).encode()).hexdigest()),
                           settings.ADMIN_PRIVATE_KEY)


def sendPoints(address, amount):
    return sendTransaction(settings.CIRCLE_TOKEN_CONTRACT.functions.transfer(address, amount),
                           settings.ADMIN_PRIVATE_KEY)
