import random
import string

QUANTIDADE = int(input("Quantos IDs necessários? "))

for i in range(QUANTIDADE):
    id = "".join([random.choice(string.digits) for i in range(12)])
    print(id)