from web3 import Web3

from solcx import compile_source

import datetime


def get_abi(fn):
    with open(fn,"r") as f:
      q=f.read()
    ret=compile_source(q)
    return ret.popitem()[1]["abi"]
def getbyaddress(address):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))


    source_file="../contracts/Notary.sol"

    #source_file="../contracts/Scream.sol"
    #address="0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"




    abi=get_abi(source_file)

    c=w3.eth.contract(address=address,abi=abi)

    key=c.functions.key().call()
    time=c.functions.time().call()
    t2=datetime.date.fromtimestamp(time)


    return key,t2
    #print(key,time)
    #print(t2)


def applytoaddress(address,what):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))


    source_file="../contracts/Notary.sol"

    #source_file="../contracts/Scream.sol"
    #address="0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"




    abi=get_abi(source_file)

    c=w3.eth.contract(address=address,abi=abi)

    print("applying to contract",c,c.functions.init(what))

    return c.functions.init(what).call({"from":b'0x10F5A2A49a50390a2f1316084BAAB0203632C455'})




if __name__ == '__main__':
    print(getbyaddress("0x8b03Af72F1Aba25B6B2e60A81b7b3044e1ea0Bb7"))







