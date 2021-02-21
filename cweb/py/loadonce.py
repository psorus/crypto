import random


loads={}
def loadonce(nam):
    def loadonce_sub(func):
        def wrapper():
            global loads
            if nam in loads.keys():return loads[nam]
            loads[nam]=func()
            return loads[nam]
        return wrapper
    return loadonce_sub

@loadonce("num")
def testload():
    return random.randint(1000,10000)


if __name__=="__main__":
    print(testload())
    print(testload())
    print(testload())
