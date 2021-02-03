import random

"""
    COSAS A ARREGLAR:
    + Función refleja de la clase Reflector muy enrevesada.
    + ¿Necesario poner el abecedario en todas las clases?
    + Hacer Enigma.conexion con blucles. 
    + ¿número de rotores variables?
    
    FUNCIONAMIENTO REFLECTOR:
    Las letras del abecedario del reflector irán emparejadas. En el caso de que el abecedario sea impar, una de esas letras irá unida consigo misma. No pueden ir emparejadas consigo mismas a no ser que el abecedario sea impar.
    
    + Creación de la clase Rotor

    + Creación de la clase Enigma

"""
class Enigma():

    def __init__(self, mensaje, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        self.rotor1 = Rotor()
        self.rotor2 = Rotor()
        self.rotor3 = Rotor()
        self.reflector = Reflector()
        self.mensaje = mensaje.upper()
        self.mensajeCodificado = ""

    def conexion(self, letra):
        abecedario = list(self.abecedario)

        posicionLetraInicial = self.abecedario.index(letra)
        posicionPrimerRotor = self.rotor1.conexion[posicionLetraInicial]
        conexionPrimerRotor = posicionPrimerRotor[1]
        posicionSegundoRotor = self.rotor2.conexion[conexionPrimerRotor]
        conexionSegundoRotor = posicionSegundoRotor[1]
        posicionTercerRotor = self.rotor3.conexion[conexionSegundoRotor]
        conexionTercerRotor = posicionTercerRotor[1]
        posicionReflector = self.reflector.configuracion[conexionTercerRotor]
        letraReflejada = posicionReflector[1]
        conexionReflectorVuelta = abecedario.index(letraReflejada)
        posicionTercerRotorVuelta = self.rotor3.conexion[conexionReflectorVuelta]
        conexionTercerRotorVuelta = posicionTercerRotorVuelta[1]
        posicionSegundoRotorVuelta = self.rotor2.conexion[conexionTercerRotorVuelta]
        conexionSegundoRotorVuelta = posicionSegundoRotorVuelta[1]
        posicionPrimerRotorVuelta = self.rotor1.conexion[conexionSegundoRotorVuelta]
        conexionPrimerRotorVuelta = posicionPrimerRotorVuelta[1]
        letraCodificada = abecedario[conexionPrimerRotorVuelta]
        
        self.mensajeCodificado += letraCodificada
        
        
            
          

    



class Reflector():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario= abecedario
        self.configuracion= [] #Guardará el reflector que se creará en la función refleja
        self.refleja()
    
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



class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario=abecedario
        cadenaPosiciones=[]
        listaNumerica = []
        self.conexion=[]
        
        contador = 0
        for i in abecedario: #Generamos una lista que irá desde el 0 hasta el total de posiciones que tiene el abecedario. Esto lo haremos para que, a la hora de crear el rotor(letra, conexión), sea más fácil.
            listaNumerica.append(contador)
            contador +=1

        for i in self.abecedario: #Asignamos cada letra con una posición.
            n = random.randrange(len(listaNumerica))
            self.conexion.append((i, listaNumerica[n]))
            listaNumerica.pop(n)

        print(listaNumerica)
        print(self.conexion)


    def codifica(self, letra): 
        n = self.abecedario.index(letra)
        m = self.conexion[n][1]
        return m

    def avanza(self):
        cadena = []
        copiaRotor = self.conexion[:]
        for i in copiaRotor:
            n = copiaRotor.index(i)
            cadena.append(copiaRotor[n][1])

        cadenaAvanza = cadena[1:]+cadena[:1]
        contador = 0
        for i in copiaRotor:
            copiaRotor[contador]= ((copiaRotor[contador][0]), cadenaAvanza[contador])
            contador +=1
        self.conexion=copiaRotor
        
        return self.conexion

    



"""
PRUEBA REFLECTOR:
r= Reflector()
r.refleja()
print(r.configuracion)

# print(len(r.abecedario))
"""
"""
PRUEBA ROTOR:
ro=Rotor()
print(ro.codifica('N'))
print(ro.avanza())
"""

# e = Enigma("Hola")
# e.codifica()
e = Enigma("F")
e.conexion("F") 