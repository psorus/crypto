from web3 import Web3

from solcx import compile_source

import datetime


def get_abi(fn):
    with open(fn,"r") as f:
      q=f.read()
    ret=compile_source(q)
    return ret.popitem()[1]["abi"]
def loadaddress(address):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))


    source_file="../sol/contracts/Page.sol"

    #source_file="../contracts/Scream.sol"
    #address="0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"


    address=Web3.toChecksumAddress(address)


    abi=get_abi(source_file)

    c=w3.eth.contract(address=address,abi=abi)

    content=c.functions.content().call()

    return content.decode("utf-8")
    #print(key,time)
    #print(t2)

def lookup(what):
    w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))


    source_file="../sol/contracts/Lookup.sol"

    #source_file="../contracts/Scream.sol"
    address="0xc840089FfA04400F4220eE07Aa5B7cD237aDeE04"#"0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"


    address=Web3.toChecksumAddress(address)


    abi=get_abi(source_file)

    c=w3.eth.contract(address=address,abi=abi)

    reg=c.functions.register(what.encode("utf-8")).call()

    return reg#content.decode("utf-8")
    #print(key,time)
    #print(t2)

def load(q):
    if len(q)>2:
        if q[:2]=="0x":
            return loadaddress(q)
    return loadaddress(lookup(q))


if __name__=='__main__':
    print(lookup("test"))
    #print(loadaddress("0x33b0cd164decc76a20cf9080e06c52e5cd7a030e"))












if __name__=='__main__':
    print(loadaddress("0x33b0cd164decc76a20cf9080e06c52e5cd7a030e"))











