import socket
from pessoa import Pessoa

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)
marcio = Pessoa()
cpf = input('Digite seu CPF')
nome = input('Digite seu nome: ')
marcio.adicionarCpf(cpf)
marcio.adicionarNome(nome)
print()
print()
opcao = int(input('Menu \n Para comprar passagem Digite 1 \n Para mais sabe preço da passagem digite 2 \n Digite:'))

if opcao == 1:
    print()
    msg = str(marcio)
    udp.sendto(msg.encode(), servidor)
    msg_servidor, servidor = udp.recvfrom(1024)
    print(msg_servidor.decode())
   
if opcao == 2:
    print('Passagem está em R$4,60 \n A meia passagem está R$2,30')