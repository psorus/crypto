from web3 import Web3

from solcx import compile_source

import datetime

from loadonce import loadonce


def get_abi(fn):
    with open(fn,"r") as f:
      q=f.read()
    ret=compile_source(q)
    return ret.popitem()[1]["abi"]
@loadonce("page")
def abi_page():
    return get_abi("../sol/contracts/Page.sol")
@loadonce("lookup")
def abi_lookup():
    return get_abi("../sol/contracts/Lookup.sol")
@loadonce("provider")
def provider():
    return Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))
def checksum(address):
    return Web3.toChecksumAddress(address)
def getcontract(w3,address,abi):
    return w3.eth.contract(address=address,abi=abi)
def loadaddress(address):
    w3=provider()
    abi=abi_page()
    address=checksum(address)
    c=getcontract(w3,address,abi)

    content=c.functions.content().call()

    return content.decode("utf-8")

def lookup(what):
    w3=provider()
    abi=abi_lookup()
    address="0xc840089FfA04400F4220eE07Aa5B7cD237aDeE04"#"0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"
    address=checksum(address)
    c=getcontract(w3,address,abi)



    reg=c.functions.register(what.encode("utf-8")).call()

    return reg#content.decode("utf-8")

def load(q):
    if len(q)>2:
        if q[:2]=="0x":
            return loadaddress(q)
    return loadaddress(lookup(q))

def getbalance(address):
    w3=provider()
    address=checksum(address)
    return w3.eth.getBalance(address)


if __name__=='__main__':
    #print(lookup("test"))
    #print(loadaddress("0x33b0cd164decc76a20cf9080e06c52e5cd7a030e"))
    print(getbalance("0x33b0cd164decc76a20cf9080e06c52e5cd7a030e"))























