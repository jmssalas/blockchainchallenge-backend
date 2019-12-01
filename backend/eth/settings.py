import hashlib
import json
import os

from eth_account import Account
from web3 import Web3, HTTPProvider

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INFURA_URL = "https://rinkeby.infura.io/v3/36ea3c28d785451c9d56f8de2d4c8a39"

TOKEN_ADDRESS = "0xe4d23f6AF6c4e4323f07EBbD46DFb772C679B628"
TRACK_ADDRESS = "0xace1Fa0bBeaC5493d2DF7f042Aaf490F6d976C6A"

ADMIN_ADDRESS = "0x1cD2280b9E44C95093f5dB5ffd60628E3EC6b63C"
ADMIN_PRIVATE_KEY = "95514A2325A3E5FE5D8EFB0A966F3744C2A089956745FF8BD12B8AD648F344F1"
SPONSOR_ADDRESS = "0x23EaD49eD2C2E731E1f3b036d7aA5996192E4012"
SPONSOR_PRIVATE_KEY = "8817d07a37f88dc9a0eff864e7ee8c926aa9105363f65afba1a38825328b9abf"

W3 = Web3(HTTPProvider(INFURA_URL))

with open(os.path.join(BASE_DIR, 'eth/circletoken_abi.json')) as f:
    abi = json.load(f)
    CIRCLE_TOKEN_CONTRACT = W3.eth.contract(address=TOKEN_ADDRESS, abi=abi)

with open(os.path.join(BASE_DIR, "eth/track_abi.json")) as f:
    abi = json.load(f)
    TRACK_CONTRACT = W3.eth.contract(address=TRACK_ADDRESS, abi=abi)
