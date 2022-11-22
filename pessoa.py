class Pessoa:
    def __init__(self, nome=None, cpf=None) -> None:
        self.nome = nome
        self.cpf = cpf

    def adicionarCpf(self, CpfCliente:str):
        self.cpf = CpfCliente
        
    def adicionarNome(self, nomeCliente):
        self.nome = nomeCliente


    def __str__(self) -> str:
        return f"{self.nome} de CPF {self.cpf}"


if __name__ == '__main__':
    teste = Pessoa()
    print('Aqui')
    teste.adicionarNome('Márcio')
    teste.adicionarCpf('14935749490')
    print(teste)