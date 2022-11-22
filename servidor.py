# Fazer o servidor multithreads.
import socket
from time import sleep
import threading

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORT))

print('Servidor no ar... Faça seu pedido')

def trata_cliente(msg, cliente):
    print('Recebi de', cliente, 'a mensagem', msg.decode())
    udp.sendto(('OK-' + msg.decode()).encode(), cliente)

while True:
    msg, cliente = udp.recvfrom(1024)
    t = threading.Thread(target=trata_cliente, args=(msg, cliente,))
    sleep(2)
    t.start()

udp.close()
