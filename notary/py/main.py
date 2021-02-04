from web3 import Web3

from solcx import compile_source


w3 = Web3(Web3.HTTPProvider('https://kovan.infura.io/v3/c83277c8952e4e1280aa1a853fb18fcf'))


source_file="../contracts/Notary.sol"
address="0xfd05cF33F75b8ff3BD53572A1dAf5b622D516318"

#source_file="../contracts/Scream.sol"
#address="0x247643ee2e8C6d4b40013245Bf7939d40E3C396e"



def get_abi(fn):
    with open(fn,"r") as f:
        q=f.read()
    ret=compile_source(q)
    return ret.popitem()[1]["abi"]

abi=get_abi(source_file)

c=w3.eth.contract(address=address,abi=abi)


print(c)




