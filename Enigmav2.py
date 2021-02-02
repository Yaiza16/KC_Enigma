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
        listaAbecedario = list(self.abecedario) #Lo convertimos en lista para poder luego trabajar con el random 
        listaBase = list(self.abecedario) #Esta la usaremos para ir quitando las letras que salgan en el random
        letrasFijas = []
        letrasVariables = []
        letraImpar = ""

        if len(listaBase)%2 == 1: #Comprobamos si el abecedario es impar o no. Si lo es, asignamos una letra que a la hora de hacer el bucle se emparejará consigo misma.
            n = random.randrange(len(listaBase))
            letraImpar = listaBase[n]


        for i in listaAbecedario:
            if i == letraImpar: #Si la letra es impar, directamente la añade.
                self.configuracion.append((i, letraImpar))
            
            else:
                YaHaSalido = False #Establecemos esta variables. Nos va a servir para identificar si la letra en el bucle for que recorre la listaAbecedario ya ha sido emparejada. Si es así, la emparejará directamente con su pareja.
                for l in letrasVariables:
                    if i == l:
                        n = letrasVariables.index(l)
                        self.configuracion.append((i, letrasFijas[n]))
                        YaHaSalido = True
                        break

                if YaHaSalido == False:   #Si la letra del abecedario todavía no ha salido, le asignará una pareja.
                    n = random.randrange(len(listaBase))
                    letra = listaBase[n]
                    while i == letra or letra == letraImpar:
                        n = random.randrange(len(listaBase))
                        letra = listaBase[n]
                    
                    self.configuracion.append((i, letra))
                    listaBase.remove(i)
                    listaBase.remove(letra)
                    letrasFijas.append(i)
                    letrasVariables.append(letra)



# class Rotor():

#     def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
#         self.abecedario=abecedario
#         self.conexion=[]
#         cadenaPosiciones=[]
#         listaNumerica = []
        
#         contador = 0
#         for i in abecedario: #Generamos una lista que irá desde el 0 hasta el total de posiciones que tiene el abecedario. Esto lo haremos para que, a la hora de crear el rotor(letra, conexión), sea más fácil.
#             listaNumerica.append(contador)
#             contador +=1

#         for i in self.abecedario: #Asignamos cada letra con una posición.
#             n = random.randrange(len(listaNumerica))
#             self.conexion.append((i, listaNumerica[n]))
#             listaNumerica.pop(n)

#         print(listaNumerica)
#         print(self.conexion)


#     def codifica(self, letra):
#         letra






r= Reflector()
r.refleja()
print(r.configuracion)

# print(len(r.abecedario))


# ro=Rotor()

