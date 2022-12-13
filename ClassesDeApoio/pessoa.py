class Pessoa:
    def __init__(self, nome=str, cpf=str) -> None:
        self.__nome = nome
        self.__cpf = cpf

    def nome(self):
        return self.__nome
    
    def cpf(self):
        return self.__cpf

    def __str__(self) -> str:
        return f"{self.__nome} CPF{self.__cpf}"

if __name__ == '__main__':
    teste = Pessoa()
    print('Aqui')
    teste.adicionarNome('Márcio')
    teste.adicionarCpf('14935749490')
    teste.adicionarDestino('João Pessoa')
    teste.adicionarTipoPagamento('Pix')
    print(teste)