import socket
from FuncoesDeApoio.pessoa import Pessoa

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)
#instaciando a classe pessoa
cliente = Pessoa()
#pegando as informações do cliente
cpf = input('Digite seu CPF: ')
nome = input('Digite seu nome: ')
destino = input('Digite seu destino: ');
tipoDePagamento = input('Digite seu tipo de Pagamento: ')
#adicionando os dados
cliente.adicionarCpf(cpf)
cliente.adicionarNome(nome)
cliente.adicionarDestino(destino)
cliente.adicionarTipoPagamento(tipoDePagamento)

print()
print()
opcao = int(input('Menu \n Para comprar passagem Digite 1: '))
quantidadeDePassagens = int(input('Quantas passagens? '))

if opcao == 1:
    msg = f" {str(cliente)}, {str(quantidadeDePassagens)}"
    udp.sendto(msg.encode(), servidor)
    msg_servidor, servidor = udp.recvfrom(1024)
    print(msg_servidor.decode())
   
