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
    dados = info.split(',')
    print(dados[0])
    print(dados[1])
    print(dados[2])
    print(dados[3])
    print(dados[4])
    print(dados[5])

    numeroPoltrona = random.randint(1,20) 
    hashTable = {dados[3]:numeroPoltrona}
    print('Hash^^')
    print(hashTable)
    print('Hash^^')
    nota= f" Cliente: {dados[1]} \n Destino:{dados[2]} \n Poltrona: {hashTable[dados[3]]} \n Data:{date.today()} \n Tipo de Pagamento: {dados[4]}"
    udp.sendto(nota.encode(), cliente)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(f'Cliente',cliente)
    print('Mesangem',msg.decode())
    t = threading.Thread(target=trata_cliente, args=(msg, cliente,))
    sleep(2)
    t.start()

udp.close()