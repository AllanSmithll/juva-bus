from .matrizEsparsa import *
from .pessoa import *

class Onibus:
    def __init__(self,id,linhas,colunas) -> None:
        self.__onibus = MatrizEsparsa(linhas,colunas)
        self.__id = id


    @property
    def id(self):
        return self.__id

    @property
    def tamanho(self):
        size = self.__onibus.tamanho
        return size
    def adicionarPassageiro(self,passageiro,poltrona):
        self.__onibus.adicionar(passageiro,poltrona)

    def exibirPoltronas(self):
        return print(self.__onibus)

    def __str__(self) -> str:
        return f'Nome do Onibus: {self.__id}'




if __name__ == '__main__':
    bus = Onibus('SMT-JPA',5,5)
    print(bus)
    print('====')
    bus.adicionarPassageiro('Márcio',2)
    bus.exibirPoltronas()
    
































