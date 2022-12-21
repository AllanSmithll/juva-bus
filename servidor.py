# Fazer o servidor multithreads.
import socket
from time import sleep
import threading
from funcoesDeGereciamento.GereciadorDeFuncoes import *
import random
HOST = 'localhost'
PORT = 5000
#criando o socket, com protocolo UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((HOST, PORT))
print('Servidor no ar... Faça seu pedido')
while True:
    msg, cliente = udp.recvfrom(1024)
    print(f'Cliente',cliente)
    print('Mesangem',msg.decode())
    t = threading.Thread(target=trata_cliente, args=(udp,msg, cliente,))
    sleep(1)
    t.start()
udp.close()
