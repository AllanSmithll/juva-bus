# Fazer o servidor multithreads.
import socket
from time import sleep
import threading
import random
from datetime import date
from FuncoesDeApoio.listaSequencial import *
from FuncoesDeApoio.hashTable import *
import random
HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORT))

print('Servidor no ar... Faça seu pedido')

# Criando a lista de poltronas desocupadas e preenchendo
listaDePoltronasDesocupadas = Lista()
for i in range(1,20):
    listaDePoltronasDesocupadas.inserir(i,i+1)
print(listaDePoltronasDesocupadas)   
#Criando a variável poltrona para o cliente


# print(poltrona)

#criando a lista de poltronas ocupadas
listaDePoltronasOcupadas = Lista()
print(listaDePoltronasOcupadas)

#toda vez que pegar um poltrona retirar da lista de desocupadas e inserir na ocupadas
# listaDePoltronasOcupadas.inserir(1,listaDePoltronasDesocupadas.remover(listaDePoltronasDesocupadas.busca(poltrona)))

print(listaDePoltronasOcupadas)
print(listaDePoltronasDesocupadas)
# if listaDePoltronasDesocupadas != None:
#      poltrona = listaDePoltronasDesocupadas[random.randint(0,10)]



def trata_cliente(msg, cliente):
    print('Recebi de', cliente, 'a mensagem', msg.decode())
    print()
    info = str(msg.decode())
    dados = info.split(',')
    print(dados[0])
    print(dados[1])
    print(dados[2])
    print(dados[3])
    print(dados[4])
    print(dados[5])
    print(dados[6])

    poltrona= listaDePoltronasDesocupadas.elemento(random.randint(0,10))
    listaDePoltronasOcupadas.inserir(1,listaDePoltronasDesocupadas.remover(listaDePoltronasDesocupadas.busca(poltrona)))
    print(listaDePoltronasOcupadas)
    print(listaDePoltronasDesocupadas)
    hashTable = {dados[2]:poltrona}
    bancoDados= ChainHashTable(10)
    
    bancoDados.put(poltrona,dados[2] )
    bancoDados.displayTable()
    print('Hash^^')
    print(hashTable)
    print('Hash^^')

    nota= f" ========Sua Nota Fiscal=======  \n Agência: 40028922 \n Cliente: {dados[0]} \n Destino:{dados[4]} \n Poltrona: {hashTable[dados[2]]} \n Data: {date.today()} \n Tipo de Pagamento: {dados[6]}"
    udp.sendto(nota.encode(), cliente)

while True:
    msg, cliente = udp.recvfrom(1024)
    print(f'Cliente',cliente)
    print('Mesangem',msg.decode())
    t = threading.Thread(target=trata_cliente, args=(msg, cliente,))
    sleep(1)
    t.start()

udp.close()