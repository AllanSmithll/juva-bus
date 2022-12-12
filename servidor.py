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
#criando o socket, com protocolo UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp.bind((HOST, PORT))

print('Servidor no ar... Faça seu pedido')

# Criando a lista de poltronas desocupadas e preenchendo
listaDePoltronasDesocupadas = Lista()
for i in range(1,20):
    listaDePoltronasDesocupadas.inserir(i,i+1)
print(listaDePoltronasDesocupadas)   
#Criando a variável poltrona para o cliente




#criando a lista de poltronas ocupadas
listaDePoltronasOcupadas = Lista()
print(listaDePoltronasOcupadas)

#toda vez que pegar um poltrona retirar da lista de desocupadas e inserir na ocupadas
# listaDePoltronasOcupadas.inserir(1,listaDePoltronasDesocupadas.remover(listaDePoltronasDesocupadas.busca(poltrona)))

print(listaDePoltronasOcupadas)
print(listaDePoltronasDesocupadas)


bancoDados= ChainHashTable(10)
#implementando o mutexPoltrona para impedir que uma mesma poltrona seja recebida por dois clientes
mutexPoltrona = threading.Semaphore(1)
mutexCliente=  threading.Semaphore(2)

def passagemPreco(tipo:str,quantidade:int):
    tipo.lower()
    print(quantidade)
    print(tipo)
    if tipo == 'pix' or tipo =='dinheiro':
        preco = 4,60 * quantidade
        pagamento = str(preco)
    elif tipo =='meia':
        preco = 2,30 * quantidade
        pagamento = str(preco)
    return pagamento

def trata_cliente(msg, cliente):
    mutexPoltrona.acquire()
    print('Recebi de', cliente, 'a mensagem', msg.decode())
    print()
    info = str(msg.decode())
    dados = info.split(',')
    # print(dados[0])
    # print(dados[1])
    # print(dados[2])
    # print(dados[3])
    # print(dados[4])
    # print(dados[5])
    # print(dados[6])
    # print(dados[7])
    nomeCliente = dados[0]
    CpfCliente = dados[2]
    DestinoCliente = dados[4]
    tipoDePagamento= dados[6]
    quantidadePassagens = int(dados[7])
    billcliente = passagemPreco(tipoDePagamento,quantidadePassagens)
    
    #destiando poltrona
    poltrona= listaDePoltronasDesocupadas.elemento(random.randint(1,19))
    listaDePoltronasOcupadas.inserir(1,listaDePoltronasDesocupadas.remover(listaDePoltronasDesocupadas.busca(poltrona)))
    print(listaDePoltronasOcupadas)
    print(listaDePoltronasDesocupadas)
    # hashTable = {dados[2]:poltrona}
   
    
    bancoDados.put(poltrona,CpfCliente)
    bancoDados.displayTable()

    nota = f" ========Sua Nota Fiscal=======  \n Agência: 40028922 \n Cliente: {nomeCliente} \n Destino: {DestinoCliente} \n Poltrona: {poltrona} \n Data: {date.today()} \n Tipo de Pagamento: {tipoDePagamento} \n Quantidades de Passagens: {quantidadePassagens} \n Preço à Pagar: {billcliente}"
    udp.sendto(nota.encode(), cliente)
    print('mutexPoltrona liberado')
    mutexPoltrona.release()


        
while True:
    mutexCliente.acquire()
    msg, cliente = udp.recvfrom(1024)
    print(f'Cliente',cliente)
    print('Mesangem',msg.decode())
    t = threading.Thread(target=trata_cliente, args=(msg, cliente,))
    sleep(1)
    t.start()
   
    
    mutexCliente.release()

udp.close()