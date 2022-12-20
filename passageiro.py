import socket
from ClassesDeApoio.pessoa import Pessoa
from ClassesDeApoio.onibus import *
from pathlib import Path
from time import sleep

# configurando main
largura = 4
comprimento = 12
path = str(Path(__file__).parent.resolve())+'/'
HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)
#instaciando a classe pessoa

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
while True:
    escolha = input("""O que deseja? 
    Buy - Para comprar passagem/passagens
    Menu - Ver linhas disponíveis
    >> """).upper()
    if escolha == "BUY":
        print('===========Linhas Disponíveis===========')
        for bus in list(onibus.keys()):
                    print(bus)
            

        cpf = input('Digite seu CPF: ')
        nome = input('Digite seu nome: ')
        linha = input('Digite a linha desejada:' )
        poltrona = input('Digite a Poltrona: ')
        cliente = f"{cpf},{nome},{linha},{poltrona}"


        msg = cliente
        udp.sendto(msg.encode(), servidor)
        msg_servidor, servidor = udp.recvfrom(1024)
        print(msg_servidor.decode())

    elif escolha == "MENU":
        print('===========Linhas Disponíveis===========')
        for bus in list(onibus.keys()):
                    print(bus)
        sleep(1.5)