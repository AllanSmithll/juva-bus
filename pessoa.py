class Pessoa:
    def __init__(self,nome=None ,cpf=None) -> None:
        nome = nome
        cpf = cpf

    def adicionarCPf(self,CpfCliente:str):
        self.cpf = CpfCliente
        
    def adicionarNome(self,nomeCliente):
        self.nome = nomeCliente


    def __str__(self) -> str:
        return self.nome,self.cpf


if __name__ == 'Main':
    marcio = Pessoa()
    print('Aqui')
    marcio.adicionarNome('Márcio')
    marcio.adicionarCPf('14935749490')

    print(marcio)



teste = Pessoa()
teste.adicionarCPf('115151')
teste.adicionarNome('Marcio')
print(teste)
print('Aaqui')