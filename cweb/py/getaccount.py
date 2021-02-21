from eth_account import Account
import json



def getaccount():

    with open("../sol/secrets.json","r") as q:
        phrase=json.loads(q.read())["mnemonic"]


    Account.enable_unaudited_hdwallet_features()
    acc = Account.from_mnemonic(phrase)

    return acc


