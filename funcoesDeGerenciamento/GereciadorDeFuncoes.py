import threading
from datetime import date
import socket
from ClassesDeApoio.onibus import *
from ClassesDeApoio.pessoa import *
from .ChainingHashTable import *
# from .geraID import *

status = {
    "OK": "200-OK",
    "EXIT": "150-CUSTOMER LEFT",
    "ERROR": "100-ERROR"
}

global banco 
banco = ChainingHashTable()
largura = 6
comprimento = 6
mutexPoltrona = threading.Semaphore(1)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Gustavo", 7), 4)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Leonidas", 5),2)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Alex Sandro", 3),5)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Allan", 10), 3)

def trata_cliente(udp,msg,cliente):
        ''' Método que serve para trata a mensagem do cliente, e devolve uma mensagem para o servidor '''
        comando = msg.decode()
        comando = comando.split(',')
        data = msg.decode()
        print(data)
        comando = comando[0]  
        print(comando)
        if comando == 'BUY':
            udp.sendto('BUY'.encode(), cliente)


        elif comando == 'ALOCAR':
            info = data.split(',')
            nomeCliente = info[1]
            CpfCliente = info[2]
            linhaCliente = str(info[3])
            poltrona = int(info[4])
            

            hashtableThread = threading.Thread(target=bancoDeDados, args=(banco,CpfCliente,poltrona))
            hashtableThread.start()
            #cria nova linha caso não haja uma com o mesmo nome
            # mutexPoltrona.acquire()
            if linhaCliente not in onibus:
                onibus[linhaCliente] = Onibus(linhaCliente, largura, comprimento)

                print("\nNOVA LINHA CRIADA\n")
            # mutexPoltrona.release()

            passageiro = Pessoa(nomeCliente,CpfCliente)
        
            # converte poltrona caso não seja informada
            if poltrona == "":
                poltrona = None
            
            else:
                poltrona = int(poltrona)

            onibus[linhaCliente].adicionarPassageiro(passageiro.nome, poltrona)
            onibus[linhaCliente].exibirPoltronas()
            print()

            #adiciona passageiro
            # mutexPoltrona.acquire()
            try:
                onibus[linhaCliente].adicionarPassageiro(passageiro.nome, poltrona)
                onibus[linhaCliente].exibirPoltronas()
            except:
                error = f'{status["ERROR"]}: operação não foi concluída'
            # mutexPoltrona.release()

            nota = f" \n  ========Sua Nota Fiscal=======  \n Emitido pela Agência: 40028922 \n Data:{date.today()} \n Cliente: {nomeCliente} \n Linha: {linhaCliente}\n Poltrona:{poltrona} "
            onibusCliente =str(onibus[linhaCliente].exibirPoltronas())
            resposta = f'{status["OK"]} \n {nota} \n {onibusCliente}'
            udp.sendto(resposta.encode(), cliente) 

        elif comando == 'MENU':
            linhas = f'{status["OK"]} \n LINHAS DISPONÌVEIS: \n SMT-JPA \n JPA-SMT'
            udp.sendto(linhas.encode(),cliente)
        
        elif comando == 'DISPLAY':              
            onibusSMT = str(onibus['SMT-JPA'].exibirPoltronas())
            onibusJPA=  str(onibus['JPA-SMT'].exibirPoltronas())          
            data = f'{status["OK"]} \n SMT-JPA\n{onibusSMT} \n JPA-SMT\n{onibusJPA}'
            udp.sendto(data.encode(),cliente)

        elif comando == 'QUIT':
            temp = str(banco)
            udp.sendto(temp.encode(),cliente)
            udp.sendto(f'{status["EXIT"]}'.encode(),cliente)
        else:
            raise f'{status["ERROR"]}: digite um comando válido.'

def bancoDeDados(banco,cpf,poltrona):
    ''' Método que retorna o relatório de compras provido pela Juva Bus. '''
    banco.put(cpf,poltrona)
    print('=========Relatorio de Compras=========')
    banco.displayTable()
    print(banco)

