import random
import mainmoduleid


def hello():
    print("Hello Kambing")

hello()



def hello (namaUser):
    print("123", namaUser)

hello("Victor")

def gachaRaidenShogun():
    num = ["Raiden", "Mei", "Shogun", "Jean", "Qiqi", "Mona", "Barbara"]
    return random.choice(num)

print(gachaRaidenShogun())

def add(x, y, z = 0):
    return x + y + z

print(add(3,5))

def localScope():
    local = 10
#print (local)

def func_luar():
    y = 20
   
    def func_dalam():
        print (y)
        
    func_dalam()
