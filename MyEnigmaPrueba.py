import random

rotor_pruebas = [('A', 'I'), ('B', 'C'), ('C', 'S'), ('D', 'E'), ('E', 'V'), ('F', 'K'), ('G', 'L'), ('H', 'Z'), ('I', 'R'), ('J', 'A'), ('K', 'N'), ('L', 'Ñ'), ('M', 'D'), ('N', 'U'), ('Ñ', 'J'), ('O', 'F'), ('P', 'W'), ('Q', 'M'), ('R', 'P'), ('S', 'B'), ('T', 'O'), ('U', 'Q'), ('V', 'X'), ('W', 'T'), ('X', 'Y'), ('Y', 'H'), ('Z', 'G')]

class Rotor():

    def __init__(self, abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario = abecedario
        otrasLetras = list(self.abecedario)
        self.rotor=[]
        self.mensajeCodificado=""
        for l in self.abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l, otrasLetras[n]))
            otrasLetras.pop(n)

        self.rotorC = rotor_pruebas[:]

    def startCodificar(self, letraInicio, mensaje):
        self.__letraInicio = letraInicio
        self.__mensaje = mensaje
        self.posicionInicial(letraInicio)
        self.codifica(mensaje)
        

    def startDescodificar(self, letraInicio, mensaje):
        self.__letraInicio = letraInicio
        self.__mensaje = mensaje
        self.posicionInicial(letraInicio)
        self.descodifica(mensaje)



    def posicionInicial(self, letra):
        position = self.abecedario.index(letra)
        self.rotorC = rotor_pruebas[position:]+rotor_pruebas[:position]
        return self.rotorC


    def avanza(self):
        self.rotorC = self.rotorC[1:]+self.rotorC[:1]
        return self.rotorC


    def codifica(self, mensaje):
        for i in mensaje:
            i=i.upper()
            try:
                if i == " ":
                    print(" ", end="")
                    self.mensajeCodificado += i
                else:
                    pLetra = self.abecedario.index(i)
                    letraCodificada = self.rotorC[pLetra][1]
                    self.mensajeCodificado += letraCodificada
                    print(letraCodificada, end="")
                    self.avanza()
            except ValueError:
                print("{} no pertenece al abecedario".format(mensaje))   


    def descodifica(self, mensaje):
        for l in mensaje: 
            l=l.upper()
            contador = -1
            if l == " ":
                print(" ", end="")
            else:
                for i in self.rotorC:
                    contador += 1
                    if i[1] == l:
                        indice = contador
                        print(self.abecedario[indice], end="")
                        self.avanza()
                        break

         

r = Rotor()
print(r.posicionInicial('C'))
r.startCodificar('C', 'Mi Casa')
print()
r.startDescodificar('C', r.mensajeCodificado)

# print(r.posicionInicial('C'))
# print(r.avanza())

# print(r.codifica('CASA'))
# print(r.descodifica('A'))
