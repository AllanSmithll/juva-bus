import random
import string

def geraId(ids):
    ''' Método que gera uma quantidade de ID '''
    ids = int(input("Quantos IDs necessários? "))

    for i in range(ids):
        id = "".join([random.choice(string.digits) for i in range(12)])
        print(id)

identifiers = geraId(5)
print(identifiers)