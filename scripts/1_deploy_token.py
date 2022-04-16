from brownie import (
    MToken,
    config,
    network,
    accounts
)
from scripts.utils import get_account
from web3 import Web3

def main():
    deploy_token()

INITIAL_SUPPLY = Web3.toWei(1000,"ether")

def deploy_token():
    account = get_account()
    mToken = MToken.deploy(INITIAL_SUPPLY,
     {"from": account},
      publish_source=config["networks"][network.show_active()].get("verify", False))
    print(mToken.name())