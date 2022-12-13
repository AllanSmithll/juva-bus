from Onibus import Onibus

class Gerenciador:
    def cadastrarOnibus(self, nome, destino, horario, quantPoltronas):
        self.__nome = nome
        self.__destino = destino
        self.__horario = horario
        self.__quantPoltronas = quantPoltronas