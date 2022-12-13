class Entry:
    """Uma classe privada utilizada para encapsular os pares chave/valor"""
    __slots__ = ( "key", "value" )
    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
        
    def __str__( self ):
        return "(" + str( self.key ) + ", " + str( self.value ) + ")"
 
class ChainHashTable:
    def __init__(self, size=10):
        self.size = size
        # inicializa a tabela de dispersão com todos os elementos iguais a None
        self.table = list([] for i in range(self.size))


    def hash(self, key:int)->int:
        ''' Método que retorna a posição na tabela hashing conforme a chave.
            Método do hash modular
        '''
        return key % self.size

    def put(self, key:int, data:object)->int:
        '''Insere um par chave/valor na tabela hash.
           Retorna o slot em que o par chave/valor foi inserido'''
        slot = self.hash(key)
        print(f'key {key} at slot {slot}')

        # verifica se a chave está no list relativo ao slot
        if key in self.table[slot]:
            return -1
        else:
            self.table[slot].append(Entry(key,data))
            return slot

    def get(self, key:int):
        '''Obtem a carga associada à chave de busca.'''
        slot = self.hash(key)
        if key not in self.table[slot]:
            return -1
        else:            
            return self.table[slot]

   
    def __str__(self):
        info = ""
        for items in self.table:
            if items == None:
                continue
            for entry in items:
                info += str(entry)
        return info

    def __len__(self):
        return self.size
         

 
    def keys(self):
        """Return a list of keys in the given hashTable.
       (It would be better to return a sequence, but that
         is too advanced.)
        """
        result = []
        for lst in self.table:
            if lst != None:
                for entry in lst:
                    result.append( entry.key )
        return result

   
    def getr( hTable, key ):
        """Return the value associated with the given key in
       the given hash table.
           Precondition: contains(hTable, key)
        """
        entry = _locate( hTable, key )
        return entry.value

    def locate( hTable, key ):
        """Find the entry in the hash table for the given key.
       If the key is not found, find the first unused location in the table.
       (This is called 'open addressing'.)
       If the entry for the key is found, that entry is returned.
       Otherwise the int index where the key would go in the table is returned.
       Finally if the key is not found and no unusued locations are left,
            the int -1 is returned.
       This function is meant to only be called from within hashtable.
       Callers of this function must be prepared to
       deal with results of two different types, unless they
       are absolutely sure whether the key is in the table
       or not.
        """
        index = self.hash( key )

        if self.table[index] == None:
            return

        for i,entry in enumerate(self.table[index]):
             if entry.key == key:
                 return i

        return -1

    def contains( self, key ):
        """Return True iff hTable has an entry with the given key."""
        entry = _locate( hTable, key )
        return isinstance( entry, _Entry )

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
            
           
if __name__ == '__main__':
    size = int(input("Enter the Size of the hash table : "))
    table1 = ChainHashTable(size)
    
    # storing elements in table
    table1.put(12,'alex')
    table1.displayTable()
    input()

    table1.put(12,'alex sandro')
    table1.displayTable()
    input()
    table1.put(31,'nathan')
    table1.put(90,'alice')

    print('len',len(table1))

    table1.put(28,'matheus')
    table1.put(88,'duda')
    table1.put(17,'jessika')
    table1.put(22,'bruno')
    table1.displayTable()
    input()
    print('get():', table1.get(12))
    table1.displayTable()