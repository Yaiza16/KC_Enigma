import random

"""
    FUNCIONAMIENTO REFLECTOR:
    Las letras del abecedario del reflector irán emparejadas. En el caso de que el abecedario
    sea impar, una de esas letras irá unida consigo misma.
    
    + Creación de la clase Rotor

    + Creación de la clase Enigma

"""

class Reflector():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario= abecedario
        self.configuracion= [] #Guardará el reflector que se creará en la función refleja
    
    def refleja(self):
        listaInicial = list(self.abecedario) #Lo convertimos en lista para poder luego trabajar con el random 
        while len(listaInicial)>= 2:
            n = random.randrange(len(listaInicial))
            m = random.randrange(len(listaInicial))
            while n == m:
                 m = random.randrange(len(listaInicial))
            nValor = listaInicial[n]
            mValor = listaInicial[m]

            self.configuracion.append((listaInicial[n], listaInicial[m]))
            listaInicial.remove(nValor) #el remove es como el pop pero, en vez de con índices, con valores
            listaInicial.remove(mValor)

        if len(listaInicial) == 1: #Esto se ejecutará cuando la listaInicial (antes de quitar ningún valor) sea impar
            self.configuracion.append((listaInicial[0], listaInicial[0]))


class Rotor():


r= Reflector()
r.refleja()
print(r.configuracion)
print(len(r.abecedario))
