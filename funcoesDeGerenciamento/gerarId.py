import random
import string

def gerarId(quantId):
    ''' Método que gera uma quantidade determinada de IDs '''

    for i in range(quantId):
        id = "".join([random.choice(string.digits) for i in range(12)])
        print
    return id
