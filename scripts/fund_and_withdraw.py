from brownie import FundMe
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def fund(fund_me):
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw(fund_me):
    account = get_account()
    print("Withdrawing...")
    fund_me.withdraw({"from": account})


def main():
    fund_me = deploy_fund_me()
    fund(fund_me)
    withdraw(fund_me)
