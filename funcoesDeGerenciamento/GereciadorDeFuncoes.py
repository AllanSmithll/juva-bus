import threading
from datetime import date
import socket
from ClassesDeApoio.onibus import Onibus
from ClassesDeApoio.pessoa import Pessoa
from .ChainingHashTable import ChainingHashTable
from .gerarId import *

status = {
    "OK": "200-OK",
    "EXIT": "150-CUSTOMER LEFT",
    "ERROR": "100-ERROR"
}

global banco 

banco = ChainingHashTable()
largura = 5
comprimento = 5
mutexPoltrona = threading.Semaphore(1)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}


def trata_cliente(udp,msg,cliente):
        comando = msg.decode()
        comando = comando.split(',')
        data = msg.decode()
        comando = comando[0]  
        if comando == 'BUY':
            udp.sendto(f'BUY'.encode(), cliente)


        elif comando == 'ALOCAR':
            info = data.split(',')
            nomeCliente = info[1]
            CpfCliente = info[2]
            linhaCliente = str(info[3])
            poltrona = int(info[4])

            mutexPoltrona.acquire()
            #cria nova linha caso não haja uma com o mesmo nome
            if linhaCliente not in onibus:
                onibus[linhaCliente] = Onibus(linhaCliente, largura, comprimento)
                print("\nNova Linha adicionada a Frota!\n")            
            mutexPoltrona.release()  
            passageiro = Pessoa(nomeCliente,CpfCliente)

            # converte poltrona caso não seja informada
            if poltrona == "":
                poltrona = None

        
            else:
                poltrona = int(poltrona)


            #adiciona passageiro
            mutexPoltrona.acquire()
            try:
                if onibus[linhaCliente].adicionarPassageiro(passageiro.nome, poltrona):
                        
                    onibusCliente = str(onibus[linhaCliente].exibirPoltronas())  
                    nota = f" \n  ========Sua Nota Fiscal=======  \nID de compra: {(gerarId(1))}\nEmitido pela Agência: 40028922 \nData: {date.today()} \nCliente: {nomeCliente} \nLinha: {linhaCliente}\nPoltrona:{poltrona} \n {onibusCliente} "
                    udp.sendto(nota.encode(), cliente) 
                else:
                    udp.sendto('Reiniciando, Poltrona inválida, Digite Display'.encode(), cliente) 

            except:
                error = f'{status["ERROR"]}: operação não foi concluída'
                udp.sendto(error.encode(), cliente)
            mutexPoltrona.release()
            #colocando os dados do cliente 
            hashtableThread = threading.Thread(target=bancoDeDados, args=(banco,CpfCliente,poltrona))
            hashtableThread.start()
            
        elif comando == 'MENU':
            linhas = f'{status["OK"]}\nLINHAS DISPONÌVEIS:\n SMT-JPA\n JPA-SMT'
            udp.sendto(linhas.encode(),cliente)
        
        elif comando == 'DISPLAY':              
            onibusSMT = str(onibus['SMT-JPA'].exibirPoltronas())
            onibusJPA=  str(onibus['JPA-SMT'].exibirPoltronas())        
            data = f'{status["OK"]} \n SMT-JPA\n{onibusSMT} \n JPA-SMT\n{onibusJPA}'
            udp.sendto(data.encode(),cliente) 

        elif comando == 'QUIT':
            udp.sendto('QUIT'.encode(),cliente)

        else:
            udp.sendto('Comando inválido'.encode(),cliente)

def bancoDeDados(banco,cpf,poltrona):
    ''' Método que serve para armazenar as compras efetuadas no dia '''
    data = str(date.today())
    banco.put(cpf,(poltrona,data))
    print('=========Relatorio de Compras=========')
    banco.displayTable()
