class MatrizEsparsa:
    ''' Matriz que serve para alocar os clientes no ônibus '''
    def __init__(self,linhas,colunas):
        self.__matriz = [ [ None for y in range( colunas ) ] 
             for x in range( linhas ) ]
        self.__linhas = len(self.__matriz)
        self.__colunas = len(self.__matriz[0])
        self.__unidades = int()

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
        if self.__matriz[linha][coluna] == None:
            self.__matriz[linha][coluna] = dados
            self.__unidades += 1

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
                    s += f'[ Vago ]'
                else:
                    s += f'[ {str(self.__matriz[lin][col])[:3]:^3} ]'

            s += '\n'
            
        return s

    @classmethod
    def calcularIndice(cls,poltrona,linhas):
        ''' Método que calcula os valores de cada slot da matriz '''
        linha = (poltrona-1) % linhas  
        coluna = (poltrona-1) // linhas
        return linha,coluna



