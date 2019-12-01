import hashlib
import json
import os

from eth_account import Account
from web3 import Web3, HTTPProvider

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INFURA_URL = "https://rinkeby.infura.io/v3/36ea3c28d785451c9d56f8de2d4c8a39"

TOKEN_ADDRESS = "0xD0D73441C6a16dFEA4f74819958069480E68D51D"
TRACK_ADDRESS = "0xa7F0f9faCdcF6a4F7205892c489f8231ddC6FE95"

ADMIN_ADDRESS = "0xA729127Ffcfeb220F801895AAA1b3d209d614FDB"
ADMIN_PRIVATE_KEY = "c7270f7ad95ffc07e4adb4c82ad89552649bf833c9bfb47f7433d806f553fb66"
SPONSOR_ADDRESS = "0x23EaD49eD2C2E731E1f3b036d7aA5996192E4012"
SPONSOR_PRIVATE_KEY = "8817d07a37f88dc9a0eff864e7ee8c926aa9105363f65afba1a38825328b9abf"

W3 = Web3(HTTPProvider(INFURA_URL))

with open(os.path.join(BASE_DIR, 'eth/circletoken_abi.json')) as f:
    abi = json.load(f)
    CIRCLE_TOKEN_CONTRACT = W3.eth.contract(address=TOKEN_ADDRESS, abi=abi)

with open(os.path.join(BASE_DIR, "eth/track_abi.json")) as f:
    abi = json.load(f)
    TRACK_CONTRACT = W3.eth.contract(address=TRACK_ADDRESS, abi=abi)
