import socket
from ClassesDeApoio.pessoa import *
from ClassesDeApoio import *
from pathlib import Path
from time import sleep

largura = 4
comprimento = 12
path = str(Path(__file__).parent.resolve())+'/'
HOST = 'localhost'
PORT = 50000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)


onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}

while True:
    escolha = input("""O que deseja? 
    Buy - Para comprar passagem/passagens
    Menu - Ver linhas disponíveis
    Display - Para ver poltronas das linhas disponíveis
    Quit - Para sair!
    >> """).upper()
<<<<<<< HEAD
=======
    escolha = escolha.upper
>>>>>>> 8e5f63a991e6697453426a1cc56466b57cf3790a
    udp.sendto(escolha.encode(), servidor)
    comando_server, servidor = udp.recvfrom(1024)
    print(comando_server.decode())

    if comando_server.decode() == "BUY":
        print('Vamos ao cadastro!')
        cpf = input('Digite seu CPF: ')
        while True:
            if len(cpf) == 11:
                break
            else:
                print('CPF Inválido')
                cpf = input('Digite seu CPF: ')
                
        nome = input('Digite seu nome: ')
        linha = input('Digite a linha desejada:' )
        poltrona = int(input('Digite a Poltrona: '))
        cliente = f"ALOCAR,{nome},{cpf},{linha},{poltrona}"
        udp.sendto(cliente.encode(), servidor)
        msg_servidor, servidor = udp.recvfrom(1024)


    elif comando_server.decode()  == "MENU":        
        msg_servidor, servidor = udp.recvfrom(1024)
        print(msg_servidor.decode())
        sleep(1)

    elif comando_server.decode() == 'DISPLAY':
        msg_servidor, servidor = udp.recvfrom(1024)
        escolha = input("""Estas são os ônibus disponíveis. Onde tem número está desocupado. O que deseja fazer?\n
        """).upper()
        udp.sendto(escolha.encode(), servidor)
        continue

    elif comando_server.decode() == 'QUIT':
<<<<<<< HEAD
        udp.sendto(''.encode(),servidor)
        print('\nSaindo da Sessão!')
=======
        print('\nSaindo da Sessão!')
        udp.sendto(''.encode(),servidor)
>>>>>>> 8e5f63a991e6697453426a1cc56466b57cf3790a
        break

    else:
        try:
            print(msg_servidor.decode())
            continue
        except:
<<<<<<< HEAD
            print('Servido com dificuldades técnicas.')
=======
            print('Servido com dificuldades técnicas')
>>>>>>> 8e5f63a991e6697453426a1cc56466b57cf3790a
