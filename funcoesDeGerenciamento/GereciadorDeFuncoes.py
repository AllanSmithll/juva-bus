import threading
from datetime import date
import socket
from ClassesDeApoio.onibus import *
from ClassesDeApoio.pessoa import *
from .ChainingHashTable import *
from .geraId import *

global banco 
banco = ChainingHashTable()
largura = 5
comprimento = 5
mutexPoltrona = threading.Semaphore(1)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Gustavo", 7), 4)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Leonidas", 5),2)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Alex Sandro", 3),5)
onibus["SMT-JPA"].adicionarPassageiro(Pessoa("Allan", 10), 3)

def trata_cliente(udp,msg,cliente):
        comando = msg.decode()
        comando = comando.split(',')
        data = msg.decode()
        comando = comando[0]  
        if comando == 'BUY':
            udp.sendto('BUY'.encode(), cliente)


        elif comando == 'ALOCAR':
            info = data.split(',')
            nomeCliente = info[1]
            CpfCliente = info[2]
            linhaCliente = str(info[3])
            poltrona = int(info[4])
            mutexPoltrona.acquire()
            if linhaCliente not in onibus:
                onibus[linhaCliente] = Onibus(linhaCliente, largura, comprimento)
                print("\nNOVA LINHA CRIADA\n")
                
            mutexPoltrona.release()  

            onibus[linhaCliente].adicionarPassageiro(Pessoa(nomeCliente,CpfCliente),4)
            onibus[linhaCliente].adicionarPassageiro(Pessoa('Teste',CpfCliente),4)
            
            hashtableThread = threading.Thread(target=bancoDeDados, args=(banco,CpfCliente,poltrona))
            hashtableThread.start()
            #cria nova linha caso não haja uma com o mesmo nome
            

           
            nota = f" \n  ========Sua Nota Fiscal=======  \n ID de compra: {geraId(1)}\n Emitido pela Agência: 40028922 \n Data:{date.today()} \n Cliente: {nomeCliente} \n Linha: {linhaCliente}\n Poltrona:{poltrona} "
            udp.sendto(nota.encode(), cliente) 

            passageiro = Pessoa(nomeCliente,CpfCliente)
        
            # converte poltrona caso não seja informada
            if poltrona == "":
                poltrona = None
            
            else:
                poltrona = int(poltrona)


            #adiciona passageiro
            mutexPoltrona.acquire()
            try:
                onibus[linhaCliente].adicionarPassageiro(passageiro.nome, poltrona)
                onibus[linhaCliente].exibirPoltronas()
            except:
                error = 'ERROR: operação não foi concluída'
                udp.sendto(error.encode(), cliente)
            mutexPoltrona.release()
            
            
        elif comando == 'MENU':
            linhas = f'200-OK \n LINHAS DISPONÌVEIS: \n SMT-JPA \n JPA-SMT'
            udp.sendto(linhas.encode(),cliente)
        
        elif comando == 'DISPLAY':              
            onibusSMT = str(onibus['SMT-JPA'].exibirPoltronas())
            onibusJPA=  str(onibus['JPA-SMT'].exibirPoltronas())
            onibusNew          
            data = f'200-OK \n SMT-JPA\n{onibusSMT} \n JPA-SMT\n{onibusJPA}'
            udp.sendto(data.encode(),cliente) 

        elif comando == 'QUIT':
            temp = str(banco)
            udp.sendto(temp.encode(),cliente)
            udp.sendto(''.encode(),cliente)
        else:
            udp.sendto('Comando inválido'.encode(),cliente)

def bancoDeDados(banco,cpf,poltrona):
    banco.put(cpf,poltrona)
    print('=========Relatorio de Compras=========')
    banco.displayTable()
    print(banco)

