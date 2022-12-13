class PosicaoInvalidaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class ValorInexistenteException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
       da lista, indicado pelo usuário, é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)
        
class Lista:
    """A classe Lista.py implementa a estrutura de dados Lista.
       A princípio, a classe está apta a manusear strings ou dados de qualquer
       tipo primitivo. É possivel armazenar objetos, porém, a recuperação
       precisa de ajustes.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             lista
    """
    def __init__(self):
        """ Construtor padrão da classe Lista sem argumentos. Ao instanciar
            um objeto do tipo Lista, este iniciará vazio. 
        """
        self.__dado = []



    def estaVazia(self):
        """ Método que verifica se a lista está vazia ou não

        Returns:
            boolean: True se a lista estiver vazia, False caso contrário

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            if(lst.estaVazia()): #
               # instrucoes
        """
        return True if len(self.__dado)==0 else False

    def tamanho(self):
        """ Método que consulta a quantidade de elementos existentes na lista

        Returns:
            int: um número inteiro que determina o número de elementos existentes na lista

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            print (lst.tamanho()) # exibe 4
        """        
        return len(self.__dado)


    def elemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
        
        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            posicao = 5
            print (lst.elemento(3)) # exibe 30
        """
        try:
            assert posicao > 0
            return self.__dado[posicao-1]
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para a Lista')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def modificar(self, posicao, valor):
        """ Método que altera o conteúdo armazenado em um elemento específico da lista

        Args:
            posicao (int): um número correpondente à ordem do elemento existente na lista
            valor (qualquer tipo primitivo): o novo valor que vai ser armazenado no elemento Ei
        
        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examplo de uso:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            posicao = 3
            lst.modificar( posicao, 55)
            print (lst.elemento( posicao )) # exibe 55
        """
        try:
            assert posicao > 0
            self.__dado[posicao-1] = valor
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para a Lista')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    
    def busca(self, valor):
        """ Método que recupera a posicao ordenada, dentro da lista, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será levada em conta

        Args:
            valor (tipo primitivo): um número/string que deseja procurar na lista
        
        Returns:
            int: um número inteiro representando a posição, na lista, em que foi
                 encontrado "valor".

        Raises:
            ValorInexistenteException: Exceção lançada quando o argumento "valor"
                  não está presente na lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            print (lst.elemento(40)) # exibe 4
        """
        try:
            return self.__dado.index(valor) + 1
        except ValueError:
            raise ValorInexistenteException(f'O valor {valor} não está armazenado na lista')
        except:
            raise

    def inserir(self, posicao, valor ):
        """ Método que adiciona um novo valor à lista

        Args:
            posicao (int): um número correpondente à posição em que se deseja
                  inserir um novo valor
            valor (qualquer tipo primitivo): o conteúdo que deseja armazenar
                  na lista.

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            lst.insere(3,50)
            print(lst)  # exibe [10,20,50,30,40]
        """
        try:
            assert posicao > 0
            self.__dado.insert(posicao-1,valor)
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para a Lista')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def remover(self, posicao):
        """ Método que remove um elemento da lista e devolve o conteudo
            existente na ordem indicada.

        Args:
            posicao (int): um número correpondente à ordem do elemento na lista
        
        Returns:
            qualquer tipo primitivo: o valor encontrado no elemento removido

        Raises:
            PosicaoInvalidaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = lst.remover(2)
            print(lst) # exibe [10,30,40]
            print(dado) # exibe 20
        """
        try:
            assert posicao > 0
            if (len(self.__dado)==0):
                raise PosicaoInvalidaException(f'A lista está vazia! Não é possivel remover elementos')
            valor = self.__dado[posicao-1]
            del self.__dado[posicao-1]
            return valor
        except IndexError:
            raise PosicaoInvalidaException(f'Posicao {posicao} invalida para remoção')
        except TypeError:
            raise PosicaoInvalidaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PosicaoInvalidaException(f'A posicao não pode ser um número negativo')
        except:
            raise


    def imprimir(self):
        """ Método que exibe a sequência ordenada dos elementos da lista

        Examples:
            lst = Lista()
            ...   # considere que temos internamente a lista [10,20,30,40]            
            lst.imprimir()) # exibe Lista: [10,20,30,40]
        """  
        print('Lista: ',end='')
        print(self.__dado)


        
    def __str__(self):
        return self.__dado.__str__()
       


lst = Lista()
try:
  
    # print(lst.elemento(-8))
    #print(lst.elemento(10))
    #print(lst.elemento('a'))
 
    #lst.busca(40)
    print('Inserindo o valor 50 na 2a posicao')
    lst.inserir(2,50)
    print('Valor inserido com sucesso!')
    print(lst)
    valor = lst.remover(4)
    print('valor:',valor)
    print(lst)
    #valor = lst.remover(10)
    lst.imprimir()
except PosicaoInvalidaException as pie:
    print(pie)
except ValorInexistenteException as vie:
    print(vie)    
except Exception as e:
    print('Nossos engenheiros vao analisar esse problema')
    
    
