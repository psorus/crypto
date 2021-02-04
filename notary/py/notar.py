from testbyadd import *
import hashlib


def hash(q):
    if type(q) is str:
        q=q.encode("utf-8")
    m=hashlib.sha256()
    m.update(q)
    return m.digest()


address="0xfd05cF33F75b8ff3BD53572A1dAf5b622D516318"
address="0x8b03Af72F1Aba25B6B2e60A81b7b3044e1ea0Bb7"

tohash="Hello World"

shallenter=False



h=hash(tohash)

if shallenter:

    print("please apply")
    print("!!!!!")
    print(h.hex())
    print("!!!!!")
    #applytoaddress(address,h)

else:

    key,time=getbyaddress(address)

    print(key)
    print(h)

    print(h==key)

    print("@",time)







