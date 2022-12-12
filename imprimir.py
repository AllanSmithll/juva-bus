from datetime import date
import random
from threading import Semaphore, Thread
mutex = Semaphore(1)
listaDePoltronasDesocupadas= [0,1,2,3,4,5,6,7,8,9,10]

if listaDePoltronasDesocupadas != None:
    poltrona= listaDePoltronasDesocupadas[random.randint(0,10)]
    print(f' ----------Nota fiscal------- \n Emitido em: São Miguel de Taipu \n Agência: 40028922 \n Origem: Local atual \n Destino:João Pessoa-PB \n Data/Hora:{date.today()}  \n Poltrona: {poltrona} ' )
    listaDePoltronasOcupadas= []
    temp = 0
    listaDePoltronasOcupadas.append(listaDePoltronasDesocupadas.pop(poltrona))
    print()
    print('Lista de Poltronas Desocupadas: ',listaDePoltronasDesocupadas)
    print('Lista de Poltronas Ocupadas: ',listaDePoltronasOcupadas)