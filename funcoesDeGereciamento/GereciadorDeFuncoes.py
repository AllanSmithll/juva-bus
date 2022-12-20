import threading
from datetime import date
import socket
from ClassesDeApoio.onibus import *
from ClassesDeApoio.pessoa import *
from pathlib import Path


# configurando main
largura = 4
comprimento = 12
path = str(Path(__file__).parent.resolve())+'/'
mutexPoltrona = threading.Semaphore(1)
mutexCliente=  threading.Semaphore(2)

onibus = {"SMT-JPA": Onibus("SMT-JPA", largura, comprimento), "JPA-SMT": Onibus("JPA-SMT", largura, comprimento)}
onibus["SMT-JPA"].alocar(Pessoa("Alex Sandro", 123))
onibus["SMT-JPA"].alocar(Pessoa("Madu", 456), 8)
onibus["SMT-JPA"].alocar(Pessoa("Macaúbas", 789), 16)
onibus["SMT-JPA"].alocar(Pessoa("Sam", 101112), 30)




def trata_cliente(udp,msg,cliente):
        info = str(msg.decode())
        dados = info.split(',')
        nomeCliente = dados[0]
        CpfCliente = dados[1]
        linhaCliente = str(dados[2])
        poltrona = int(dados[3])
    
         #cria nova linha caso não haja uma com o mesmo nome
        if linhaCliente not in onibus:
            onibus[linhaCliente] = Onibus(linhaCliente, largura, comprimento)

            print("\nNOVA LINHA CRIADA\n")


        passageiro = Pessoa(nomeCliente,CpfCliente)
     
        # converte poltrona caso não seja informada
        if poltrona == "":
            poltrona = None
        
        else:
            poltrona = int(poltrona)

        print()

        #adiciona passageiro
        try:
            onibus[linhaCliente].alocar(passageiro, poltrona)
            # onibus[linhaCliente].exibirOnibus()
        except OnibusException as oe:
            print(oe)


      
        nota = f" \n ========Sua Nota Fiscal=======  \n Emitido pela Agência: 40028922 \n Data:{date.today()} \n Cliente: {nomeCliente} \n Linha: {linhaCliente}\n Poltrona:{poltrona} \n  "
        
        udp.sendto(nota.encode(), cliente)
          

def obterDados(msg):



    info = str(msg.decode())
    dados = info.split('')
    nomeCliente = dados[0]
    CpfCliente = dados[1]
    linhaCliente = dados[2]
    poltrona = dados[3]

    return nomeCliente,CpfCliente,linhaCliente,poltrona

print(onibus)