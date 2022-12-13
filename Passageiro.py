import socket
from Pessoa import Pessoa

HOST = 'localhost'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor = (HOST, PORT)

marcio = Pessoa()

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
opcao = int(input('============= Menu ============= \nPara comprar passagem, digite 1: \nPara mais saber preço da passagem, digite 2: \nDigite: '))

while True:
    if opcao == 1:
        print()
        msg = str(marcio)
        udp.sendto(msg.encode(), servidor)
        msg_servidor, servidor = udp.recvfrom(1024)
        print(msg_servidor.decode())
   
    if opcao == 2:
        print('- Passagem está em R$4,60 \n- A meia passagem está R$2,30')
        comprar = input("Quer fazer uma compra (S ou N)? ").upper()
        opcao = int(input('============= Menu ============= \nPara comprar passagem, digite 1: \nPara mais saber preço da passagem, digite 2: \nDigite: '))
        
opcao = int(input('Menu \n Para comprar passagem Digite 1: '))
quantidadeDePassagens = int(input('Quantas passagens? '))

if opcao == 1:
    msg = f" {str(cliente)}, {str(quantidadeDePassagens)}"
    udp.sendto(msg.encode(), servidor)
    msg_servidor, servidor = udp.recvfrom(1024)
    print(msg_servidor.decode())
