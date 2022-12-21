import threading
from datetime import date
import socket
from ClassesDeApoio.onibus import *
from ClassesDeApoio.pessoa import *
from pathlib import Path


# configurando main
largura = 5
comprimento = 5
path = str(Path(__file__).parent.resolve())+'/'
mutexPoltrona = threading.Semaphore(1)
mutexCliente=  threading.Semaphore(2)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Alex Sandro", 3),5)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Leonidas", 5),2)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Gustavo", 7), 4)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Allan", 10), 3)

def trata_cliente(udp,msg,cliente):
        comando = msg.decode()
        comando = comando.split(',')
        comando = comando[0]  
        print(comando)
        if comando == 'BUY':
            udp.sendto('BUY'.encode(), cliente)
        elif comando == 'ALOCAR':
            # msg, cliente = udp.recvfrom(2048)
            print(msg)
            info = comando
            dados = info.split(',')
            nomeCliente = dados[1]
            CpfCliente = dados[2]
            linhaCliente = str(dados[3])
            poltrona = int(dados[4])

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

            nota = f" 200-OK \n  ========Sua Nota Fiscal=======  \n Emitido pela Agência: 40028922 \n Data:{date.today()} \n Cliente: {nomeCliente} \n Linha: {linhaCliente}\n Poltrona:{poltrona} "
            udp.sendto(nota.encode(), cliente) 

        elif comando == 'MENU':
            linhas = f'200-OK \n LINHAS DISPONÌVEIS: \n SMT-JPA \n JPA-SMT'
            udp.sendto(linhas.encode(),cliente)
        
        elif comando == 'EXIBIR':              
            temp = str(onibus['SMT-JPA'].exibirPoltronas())
            temp2 =  str(onibus['JPA-SMT'].exibirPoltronas())
            data = f'200-OK \n SMT-JPA\n{temp} \n JPA-SMT\n{temp2}'
            udp.sendto(data.encode(),cliente) 

        elif comando == 'QUIT':
            udp.sendto('QUIT'.encode(),cliente)