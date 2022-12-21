import threading


class MatrizEsparsa:
    def __init__(self,linhas,colunas):
        self.__matriz = [ [ None for y in range( colunas ) ] 
             for x in range( linhas ) ]
        self.__linhas = len(self.__matriz)
        self.__colunas = len(self.__matriz[0])
        self.__unidades = int()
        self.__adm = threading.Semaphore(1)
    @property
    def matriz(self):
        return self.__matriz

    @property
    def tamanho(self):
        return self.__linhas * self.__colunas
    @property
    def linhas(self):
        return self.__linhas
    @property
    def colunas(self):
        return self.__colunas
    @property
    def unidades(self):
        return self.__unidades

    @property
    def estaVazia(self):
        return self.__unidades == 0
    def pesquisar(self,posicao):
        (linha,coluna) = self.calcularIndice(posicao,self.__linhas)

        return self.__matriz[linha][coluna]


    def adicionar(self,dados,poltrona):

        (linha,coluna) = self.calcularIndice(poltrona,self.__linhas)
        print(linha,coluna)
        if self.__matriz[linha][coluna] == None:
            self.__matriz[linha][coluna] = dados
            self.__unidades += 1
            self.__adm.release()
            return True

    def __str__(self):
        s = ''
        temp = 1
        i = 0   
        for lin in range(self.__linhas):
            temp += self.__linhas
            for col in range(self.__colunas):
                i += 1
                if self.__matriz[lin][col] == None:
                    s += f'[ {i} ]'
                else:
                    s += f'[ {str(self.__matriz[lin][col])[:3]:^3} ]'

            s += '\n'
            
        return s

    @classmethod
    def calcularIndice(cls,poltrona,linhas):
        linha = (poltrona-1) % linhas  
        coluna = (poltrona-1) // linhas
        return linha,coluna

    @classmethod
    def indice(cls,poltrona,linhas):
        if poltrona < 6:
            linha = 0
            coluna = poltrona - 1
        elif poltrona >= 6 and poltrona < 11:
             linha = 1
             coluna =   (poltrona - 1) - 5 
        elif poltrona >= 11 and poltrona <16:
             linha = 2
             coluna =   (poltrona - 1) - 10
        elif poltrona >= 16 and poltrona < 21:
             linha = 3
             coluna =   (poltrona - 1) - 20
        elif poltrona >= 21 and poltrona <= 25:
             linha = 4
             coluna = (poltrona - 1) - 25

        return linha,coluna

if __name__ == '__main__':
    mat = MatrizEsparsa(5,5)
    print(mat)
    mat.adicionar('Márcio',25)
    print(mat)


