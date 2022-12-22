# Implementação de HashTable com tratamento de colisão por encadeamento
# Autor: Alex Sandro
from typing import List

class AbsentKeyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""

    def __init__( self, entryKey:any, entryValue:any):
        self.key = entryKey
        self.value = entryValue
        
    def __eq__(self, outroObjeto):
        '''Método que vai possibilitar comparar chaves quando a chave for um objeto de outra classe'''
        return self.key == outroObjeto.key
        
    def __str__( self )->str:
        return "(" + str( self.key ) + ":" + str( self.value ) + ")"
 
class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        # inicializa a tabela de dispersão com uma série de lists vazios
        self.table = list([] for i in range(self.size))


    def __hash(self, key:any):
        ''' Método que retorna a posição na tabela hashing conforme a chave.
            Aplicação do cálculo do hash modular.
        '''
        return hash(key) % self.size

    def put(self, key:any, value:any)->int:
        '''
        Adiciona um par chave/valor à tabela hash
        Se a chave já existir, apenas atualiza o valor correspondente
        '''
        slot = self.__hash( key )
        print(f'key {key} mapeada ao slot {slot}')

        for entry in self.table[slot]: # varre as entradas da ht para ver se já existe a chave
            if key == entry.key:
                entry.value = value # se a chave existir, altera sua carga
                return slot
            
        self.table[slot].append(Entry(key,value))
        return slot
            

    def get(self, key:any)->any:
        '''
        Obtem o valor armazenado na entrada referente à chave "key"
        '''
        slot = self.__hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i].value
        else:
            raise AbsentKeyException(f'Chave {key} inexistente na tabela hash')

   
    def __str__(self)->str:
        info = "{ "
        for items in self.table:
            # examina se o slot da tabela hash tem um list com elementos
            if items == None:
                continue
            for entry in items:
                info += str(entry)
        info += " }"
        return info

    def __len__(self)->int:
        count = 0
        for i in self.table:
            count += len(i)
        return count
         

 
    def keys(self)->List[any]:
        """Retorna uma lista com as chaves armazenadas na hashTable.
        """
        result = []
        for lst in self.table:
            if lst != None:
                for entry in lst:
                    result.append( entry.key )
        return result

    def contains( self, key:any )->bool:
        """Return True se somente se a tabela hash tem uma entrada com a chave passada
           como argumento.
        """
        entry = self.__locate( key )
        return isinstance( entry, Entry )


    def __locate(self, key)->Entry:
        '''
        Método que verifica se uma chave está presente na tabela hash e devolve a
        entrada correspondente quando a busca é realizada com sucesso
        '''
        slot = self.__hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                return self.table[slot][i]
        else:
            return None
          
    def remove(self, key:any)->Entry:
        '''
        Método que remove a entrada correspondente à chave passada como argumento
        '''
        slot = self.__hash(key)
        for i in range(len(self.table[slot])):
            if key == self.table[slot][i].key:
                entry = self.table[slot][i]
                del self.table[slot][i]
                return entry
        raise AbsentKeyException(f'Chave {key} não está presente na tabela hash') 


    def displayTable(self):
        entrada = -1
        for items in self.table:
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='') 
            if len(items) == 0:
                print(' None')
                continue
            for entry in items:
                print(f'[ {entry.key},{entry.value} ] ',end='')
            print()