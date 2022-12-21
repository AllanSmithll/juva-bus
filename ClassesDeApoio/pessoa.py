class Pessoa:
    def __init__(self, nome=str, cpf=str) -> None:
        self.__nome = nome
        self.__cpf = cpf
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf

    def __str__(self) -> str:
        return f"{self.__nome} CPF{self.__cpf}"

if __name__ == '__main__':
    teste = Pessoa()
  