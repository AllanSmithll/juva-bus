class Pessoa:
    def __init__(self, nome=None, cpf=None, destino=None, tipoDePagamento=None) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__destino = destino
        self.__tipoDePagamento = tipoDePagamento

    def adicionarCpf(self, CpfCliente:str):
        self.__cpf = CpfCliente
        
    def adicionarNome(self, nomeCliente):
        self.__nome = nomeCliente

    def adicionarDestino(self,destinoCliente):
        self.__destino = destinoCliente

    def adicionarTipoPagamento(self,tipoCliente):
        self.__tipoDePagamento = tipoCliente


    def __str__(self) -> str:
        return f"{self.__nome}, CPF,{self.__cpf}, Destino:,{self.__destino}, Tipo Pagamento:,{self.__tipoDePagamento}"


if __name__ == '__main__':
    teste = Pessoa()
    print('Aqui')
    teste.adicionarNome('Márcio')
    teste.adicionarCpf('14935749490')
    teste.adicionarDestino('João Pessoa')
    teste.adicionarTipoPagamento('Pix')
    print(teste)