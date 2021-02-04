import random
"""
He creado  rotores de prueba y 3 reflectores para poder generar una máquina fija y poder hacer pruebas.
Para generar un reflector aleatorio, ejecutar Reflector().
Para generar un rotor aleatorio, ejecutar Rotor()

"""
rotor1_prueba = [('A', 'U'), ('B', 'A'), ('C', 'F'), ('D', 'C'), ('E', 'N'), ('F', 'V'), ('G', 'P'), ('H', 'I'), ('I', 'J'), ('J', 'H'), ('K', 'W'), ('L', 'E'), ('M', 'Ñ'), ('N', 'S'), ('Ñ', 'L'), ('O', 'Y'), ('P', 'K'), ('Q', 'R'), ('R', 'Q'), ('S', 'B'), ('T', 'X'), ('U', 'O'), ('V', 'D'), ('W', 'Z'), ('X', 'G'), ('Y', 'T'), ('Z', 'M')]
rotor2_prueba = [('A', 'P'), ('B', 'U'), ('C', 'Q'), ('D', 'A'), ('E', 'V'), ('F', 'O'), ('G', 'M'), ('H', 'J'), ('I', 'N'), ('J', 'R'), ('K', 'L'), ('L', 'I'), ('M', 'Ñ'), ('N', 'F'), ('Ñ', 'C'), ('O', 'H'), ('P', 'Y'), ('Q', 'E'), ('R', 'Z'), ('S', 'D'), ('T', 'K'), ('U', 'W'), ('V', 'X'), ('W', 'S'), ('X', 'T'), ('Y', 'G'), ('Z', 'B')]
rotor3_prueba = [('A', 'Z'), ('B', 'T'), ('C', 'X'), ('D', 'W'), ('E', 'N'), ('F', 'A'), ('G', 'E'), ('H', 'B'), ('I', 'O'), ('J', 'V'), ('K', 'U'), ('L', 'F'), ('M', 'S'), ('N', 'G'), ('Ñ', 'C'), ('O', 'Q'), ('P', 'I'), ('Q', 'L'), ('R', 'H'), ('S', 'M'), ('T', 'K'), ('U', 'D'), ('V', 'R'), ('W', 'Y'), ('X', 'Ñ'), ('Y', 'P'), ('Z', 'J')]
rotor4_prueba = [('A', 'N'), ('B', 'F'), ('C', 'G'), ('D', 'O'), ('E', 'U'), ('F', 'K'), ('G', 'A'), ('H', 'R'), ('I', 'B'), ('J', 'V'), ('K', 'S'), ('L', 'J'), ('M', 'C'), ('N', 'Ñ'), ('Ñ', 'D'), ('O', 'Q'), ('P', 'M'), ('Q', 'E'), ('R', 'L'), ('S', 'X'), ('T', 'T'), ('U', 'I'), ('V', 'Y'), ('W', 'H'), ('X', 'Z'), ('Y', 'W'), ('Z', 'P')]
rotor5_prueba = [('A', 'T'), ('B', 'Ñ'), ('C', 'R'), ('D', 'L'), ('E', 'P'), ('F', 'S'), ('G', 'W'), ('H', 'F'), ('I', 'E'), ('J', 'B'), ('K', 'A'), ('L', 'N'), ('M', 'J'), ('N', 'K'), ('Ñ', 'V'), ('O', 'O'), ('P', 'D'), ('Q', 'G'), ('R', 'M'), ('S', 'I'), ('T', 'Z'), ('U', 'X'), ('V', 'U'), ('W', 'Y'), ('X', 'Q'), ('Y', 'H'), ('Z', 'C')]
rotor6_prueba = [('A', 'H'), ('B', 'W'), ('C', 'L'), ('D', 'N'), ('E', 'B'), ('F', 'J'), ('G', 'V'), ('H', 'O'), ('I', 'K'), ('J', 'S'), ('K', 'U'), ('L', 'I'), ('M', 'X'), ('N', 'R'), ('Ñ', 'D'), ('O', 'M'), ('P', 'T'), ('Q', 'A'), ('R', 'Y'), ('S', 'C'), ('T', 'Z'), ('U', 'G'), ('V', 'P'), ('W', 'E'), ('X', 'Ñ'), ('Y', 'Q'), ('Z', 'F')]
rotor7_prueba = [('A', 'R'), ('B', 'Y'), ('C', 'J'), ('D', 'Q'), ('E', 'V'), ('F', 'G'), ('G', 'A'), ('H', 'F'), ('I', 'K'), ('J', 'Z'), ('K', 'D'), ('L', 'B'), ('M', 'O'), ('N', 'S'), ('Ñ', 'C'), ('O', 'X'), ('P', 'I'), ('Q', 'E'), ('R', 'T'), ('S', 'H'), ('T', 'M'), ('U', 'N'), ('V', 'P'), ('W', 'Ñ'), ('X', 'L'), ('Y', 'U'), ('Z', 'W')]
reflector1_prueba = [('A', 'T'), ('B', 'E'), ('C', 'S'), ('D', 'W'), ('E', 'B'), ('F', 'Ñ'), ('G', 'R'), ('H', 'K'), ('I', 'P'), ('J', 'U'), ('K', 'H'), ('L', 'Q'), ('M', 'Z'), ('N', 'N'), ('Ñ', 'F'), ('O', 'X'), ('P', 'I'), ('Q', 'L'), ('R', 'G'), ('S', 'C'), ('T', 'A'), ('U', 'J'), ('V', 'Y'), ('W', 'D'), ('X', 'O'), ('Y', 'V'), ('Z', 'M')]
reflector2_prueba = [('A', 'C'), ('B', 'Q'), ('C', 'A'), ('D', 'W'), ('E', 'P'), ('F', 'R'), ('G', 'Ñ'), ('H', 'V'), ('I', 'X'), ('J', 'T'), ('K', 'N'), ('L', 'U'), ('M', 'Y'), ('N', 'K'), ('Ñ', 'G'), ('O', 'Z'), ('P', 'E'), ('Q', 'B'), ('R', 'F'), ('S', 'S'), ('T', 'J'), ('U', 'L'), ('V', 'H'), ('W', 'D'), ('X', 'I'), ('Y', 'M'), ('Z', 'O')]
reflector3_prueba = [('A', 'N'), ('B', 'Q'), ('C', 'U'), ('D', 'Z'), ('E', 'S'), ('F', 'W'), ('G', 'H'), ('H', 'G'), ('I', 'Ñ'), ('J', 'V'), ('K', 'O'), ('L', 'Y'), ('M', 'T'), ('N', 'A'), ('Ñ', 'I'), ('O', 'K'), ('P', 'X'), ('Q', 'B'), ('R', 'R'), ('S', 'E'), ('T', 'M'), ('U', 'C'), ('V', 'J'), ('W', 'F'), ('X', 'P'), ('Y', 'L'), ('Z', 'D')]

"""
    ENIGMA:
    + Nada más presionar una letra de entrada, hace que el primer rotor se mueva (Done)
    + Poner el número de rotores variables
    + Insertar muescas
    + Añadir mensaje (Done)
    + Tener en cuenta los espacios (Done)
    + Arreglar clase Rotor para qué no haya que cambiar nada si se quiere crear un nuevo rotor aleatorio (Más o menos. Por defecto crea un nuevo rotor. No comprueba que, si se intorudce una configuración, esta sea correcta)
"""

class Enigma():

    def __init__(self, posicion, mensaje, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.mensaje = mensaje.upper()
        self.abecedario = abecedario
        self.posicion = posicion
        self.rotor1 = Rotor(self.posicion[0], rotor1_prueba)
        self.rotor2 = Rotor(self.posicion[1], rotor2_prueba)
        self.rotor3 = Rotor(self.posicion[2], rotor3_prueba)
        self.reflector = Reflector(reflector1_prueba)
        self.numeroVueltasRotor1 = 0
        self.numeroVueltasRotor2 = 0
        self.numeroVueltasRotor3 = 0
        self.mensajeDesencriptado = ""

        self.codifica(self.mensaje)
        print(self.mensajeDesencriptado)

    def codifica(self, mensaje):
        for letra in mensaje:
            if letra == " ":
                self.mensajeDesencriptado += " "
            else:
                self.entradaLetra()
                indicePosicionLetra = self.abecedario.index(letra)
                tuplaRotor1 = self.rotor1.rotorC[indicePosicionLetra]
                posicionLetraRotor1 = self.abecedario.index(tuplaRotor1[1]) #Saca la letra transformada del Rotor1 y nos da la posición
                tuplaRotor2 = self.rotor2.rotorC[posicionLetraRotor1]
                posicionLetraRotor2 = self.abecedario.index(tuplaRotor2[1])
                tuplaRotor3 = self.rotor3.rotorC[posicionLetraRotor2]
                posicionLetraRotor3 = self.abecedario.index(tuplaRotor3[1])
                tuplaReflector = self.reflector.configuracion[posicionLetraRotor3]
                letraReflector = tuplaReflector[1]
                for i in self.rotor3.rotorC:
                    if letraReflector == i[1]:
                        letraRotor3Vuelta = i[0]
                        break
                for i in self.rotor2.rotorC:
                    if letraRotor3Vuelta == i[1]:
                        letraRotor2Vuelta = i[0]
                        break
                for i in self.rotor1.rotorC:
                    if letraRotor2Vuelta == i[1]:
                        letraRotor1Vuelta = i[0]
                        break
                letraDescodificada = letraRotor1Vuelta
                self.mensajeDesencriptado += letraDescodificada


    def entradaLetra(self): #Avanza el rotor1 y comprueba si los demás tienen que avanzar o no.
        self.rotor1.avanza()
        self.numeroVueltasRotor1 +=1
        if self.numeroVueltasRotor1 == len(self.abecedario):
            self.rotor2.avanza()
            self.numeroVueltasRotor2 += 1
        if self.numeroVueltasRotor2 == len(self.abecedario):
            self.rotor3.avanza()
        


class Rotor():

    def __init__(self, posicion="A", configuracion="", abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.posicion = posicion
        self.abecedario=abecedario
        self.configuracion = configuracion #Este es el rotor creado aleatoriamente
        self.rotorC = [] #Este rotor se basa en el de configuración. Cambiará según la posicionInicial y el avanza.
        
        if self.hayConfiguracion(self.configuracion) == False:
            self.configuracion = []
            otrasLetras = list(self.abecedario)
            for i in abecedario:
                n = random.randrange(len(otrasLetras))
                self.configuracion.append((i, otrasLetras[n]))
                otrasLetras.pop(n)

        self.posicionInicial()

    def posicionInicial(self): #Devuelve el rotor ya configurado
        self.letra = self.posicion
        cadena1 = []
        cadena1ordenada = []
        for i in self.configuracion:
            valor = i[1]
            cadena1.append(valor)
        posicion = cadena1.index(self.letra)
        cadena1ordenada = cadena1[posicion:]+cadena1[:posicion]
        for i in self.abecedario:
            self.rotorC.append((i, cadena1ordenada[self.abecedario.index(i)]))
        return self.rotorC

    def avanza(self):
        cadena1 = []
        cadenaAvanza = []
        rotor = []
        for i in self.rotorC:
            cadena1.append(i[1])
        
        cadenaAvanza = cadena1[1:]+cadena1[:1]
        for i in self.abecedario:
            rotor.append((i, cadenaAvanza[self.abecedario.index(i)]))
        self.rotorC = rotor
        return self.rotorC

    def hayConfiguracion(self, configuracion):
        try:
            len(configuracion) == len(self.abecedario)
        except:
            return False


class Reflector():

    def __init__(self, configuracion="", abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario= abecedario
        self.configuracion= configuracion

        if self.hayConfiguracion(self.configuracion) == False:
            self.configuracion = []
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

    def hayConfiguracion(self, configuracion):
        try:
            len(configuracion) == len(self.abecedario)
        except:
            return False

e = Enigma("YVC", "Hola soy Yaiza")
e = Enigma("YVC", "KEPB PRX JSSÑE")


r = Reflector()


"""
print(r.posicionInicial("L"))
print(r.avanza())
"""