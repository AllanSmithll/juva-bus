import threading
from datetime import date
import socket
from onibus import *
from pessoa import *
from pathlib import Path


# configurando main
largura = 4
comprimento = 12
path = str(Path(__file__).parent.resolve())+'/'
mutexPoltrona = threading.Semaphore(1)
mutexCliente=  threading.Semaphore(2)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Alex Sandro", 3),5)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Madu", 5),2)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Macaúbas", 7), 4)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Sam", 10), 3)
onibus["SMT-JPA"].exibirPoltronas()



def trata_cliente(udp,msg,cliente):
        comando = msg.decode()
        comando = comando.split(',')
        comando = comando[0]
        print(comando)

        if comando == 'BUY':
            udp.sendto('BUY'.encode(), cliente)
            msg, cliente = udp.recvfrom(2048)
            print(msg)
            info = str(msg.decode())
            dados = info.split(',')
            nomeCliente = dados[0]
            CpfCliente = dados[1]
            linhaCliente = str(dados[2])
            poltrona = int(dados[3])

            #cria nova linha caso não haja uma com o mesmo nome
            mutexPoltrona.acquire()
            if linhaCliente not in onibus:
                onibus[linhaCliente] = Onibus(linhaCliente, largura, comprimento)

                print("\nNOVA LINHA CRIADA\n")
            mutexPoltrona.release()

            passageiro = Pessoa(nomeCliente,CpfCliente)
        
            # converte poltrona caso não seja informada
            if poltrona == "":
                poltrona = None
            
            else:
                poltrona = int(poltrona)

            print()

            #adiciona passageiro
            mutexPoltrona.acquire()
            try:
                onibus[linhaCliente].adicionarPassageiro(passageiro.nome, poltrona)
                onibus[linhaCliente].exibirPoltronas()
            except:
                print('ERROR')
            mutexPoltrona.release()

        
            nota = f" \n ========Sua Nota Fiscal=======  \n Emitido pela Agência: 40028922 \n Data:{date.today()} \n Cliente: {nomeCliente} \n Linha: {linhaCliente}\n Poltrona:{poltrona} "
            
            udp.sendto(nota.encode(), cliente)
            udp.sendto('QUIT'.encode(), cliente)
        elif comando == 'MENU':
            linhas = f'LINHAS DISPONÌVEIS: \n SMT-JPA \n JPA-SMT'
            udp.sendto(linhas.encode(),cliente)
                
