# Fazer o servidor multithreads.
import socket
from time import sleep
import threading
import random
from datetime import date

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORT))

print('Servidor no ar... Faça seu pedido')

def trata_cliente(msg, cliente):
    print('Recebi de', cliente, 'a mensagem', msg.decode())
    print()
    info = str(msg.decode())
    temp = info.split()
    print(temp[0] + temp[1])
    print(temp[2] + temp[3])
    numeroPoltrona = random.randint(1,20) 
    hashTable = {temp[3]:numeroPoltrona}
    print(hashTable)
    print()
    nota= f" Cliente: {temp[1]} \n Poltrona: {hashTable[temp[3]]} \n Data:{date.today()}"
    udp.sendto(nota.encode(), cliente)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(f'Cliente',cliente)
    print('Mesangem',msg.decode())
    t = threading.Thread(target=trata_cliente, args=(msg, cliente,))
    sleep(2)
    t.start()

udp.close()