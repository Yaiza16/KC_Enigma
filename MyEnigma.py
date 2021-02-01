import random

rotor_pruebas = [('A', 'I'), ('B', 'C'), ('C', 'S'), ('D', 'E'), ('E', 'V'), ('F', 'K'), ('G', 'L'), ('H', 'Z'), ('I', 'R'), ('J', 'A'), ('K', 'N'), ('L', 'Ñ'), ('M', 'D'), ('N', 'U'), ('Ñ', 'J'), ('O', 'F'), ('P', 'W'), ('Q', 'M'), ('R', 'P'), ('S', 'B'), ('T', 'O'), ('U', 'Q'), ('V', 'X'), ('W', 'T'), ('X', 'Y'), ('Y', 'H'), ('Z', 'G')]

class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        otrasLetras = list(self.abecedario)
        self.rotor=[]
        for l in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)

        self.rotorC = self.rotor[:]

    def startCodificar(self, letraInicio, mensaje):
        self.letraInicio = letraInicio
        self.mensaje = mensaje
        self.posicionInicial(letraInicio)
        self.codifica(mensaje)

    
    def codifica(self, mensaje):
        for i in mensaje:
            try:
                pLetra = self.abecedario.index(i)
                print(self.rotorC[pLetra][1], end="")
                self.avanza()
            except ValueError:
                print("{} no pertenece al abecedario".format(mensaje))

    

    def posicionInicial(self, letra):
        position = self.abecedario.index(letra)
        self.rotorC = self.rotor[position:]+self.rotor[:position]
        return self.rotorC
    

    def avanza(self): #Solo codifica, no avanza el motor
        self.rotorC = self.rotorC[1:]+self.rotorC[:0]


    # Hay que escribir la el resultado de la letra ya codificada. Si escribimos C, nos dará la A, por tanto tenemos que poner la A.
    def descodifica(self, letra):  
        contador = 0
        for i in self.rotorC:
            contador += 1
            if i[1] == letra:
                indice = contador
                break
        return self.abecedario[indice]


r = Rotor()
print(r.codifica('S'))

print(r.posicionInicial('G'))