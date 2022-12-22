import socket
from ClassesDeApoio.pessoa import *
from ClassesDeApoio.onibus import *

from time import sleep

largura = 5
comprimento = 5

HOST = 'localhost'
PORT = 65432
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)


onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}

while True:
    print('-=-'*15)
    escolha = input("""O que deseja? 
    Buy - Para comprar passagem
    Menu - Ver linhas disponíveis
    Display - Para ver poltronas das linhas disponíveis
    Quit - Para sair!
    >> """).upper().strip()
    print("-=-"*15)

    udp.sendto(escolha.encode(), servidor)
    comando_server, servidor = udp.recvfrom(1024)
    print(comando_server.decode())

    if comando_server.decode() == "BUY":
        print('Vamos a Comprar!')
        cpf = input('Digite seu CPF: ').strip()
        while True:
            if len(cpf) == 11:
                break
            else:
                print('CPF Inválido')
                cpf = input('Digite seu CPF: ').strip()
                
        nome = input('Digite seu nome: ').strip()
        linha = input('Digite a linha desejada: ').upper()
        while True:
            if linha == 'SMT-JPA' or linha == 'JPA-SMT': break
            else:
                print(f"Linha incorreta. Lembre-se do nome das linhas: {onibus['JPA-SMT']},{onibus['SMT-JPA']}.")
                linha = input('Digite a linha desejada: ').upper().strip()

        poltrona = int(input('Digite a Poltrona: '))
        cliente = f"ALOCAR,{nome},{cpf},{linha},{poltrona}"
        udp.sendto(cliente.encode(), servidor)
        msg_servidor, servidor = udp.recvfrom(1024)
        print(msg_servidor.decode())



    elif comando_server.decode()  == "MENU":        
        msg_servidor, servidor = udp.recvfrom(1024)
        print(msg_servidor.decode())
        sleep(1)

    elif comando_server.decode() == 'DISPLAY':
        msg_servidor, servidor = udp.recvfrom(1024)
        udp.sendto(msg_servidor.encode(),servidor)
        continue

    elif comando_server.decode() == 'QUIT':
        print(f'\nSaindo da Sessão!')
        udp.sendto(''.encode(),servidor)
        break
