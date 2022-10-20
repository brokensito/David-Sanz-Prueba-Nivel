


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {}cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {} ".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h , {} cc".format(self.velocidad,self.cilindrada)

vehiculos = [Motocicleta("morado", 2, "urbana", 110, 1400), Camioneta("blanco", 4, 90, 1500, 500), 
Coche("negro", 4, 120, 1500), Bicicleta("dorado", 2, "deportiva")]

def catalogar(lista):

    for i in lista:
        print("El vehiculo {} tiene los siguientes atributos: {}".format(type(i).__name__, i))


def catalogar(lista, ruedas=None):

    if ruedas!=None: 
        cont = 0

        for i in lista:
            if i.ruedas == ruedas:
                cont +=1

        print("Se han encontrado {} vehiculos con {} ruedas:".format(cont, ruedas))

    for i in lista:
        if i.ruedas == ruedas:
            print(type(i).__name__,":", i)

        if ruedas == None:  
            print("\nEl vehiculo {} tiene los siguientes atributos: \n -  {}".format(type(i).__name__, i))

    


catalogar(vehiculos)

# catalogar(vehiculos, 2)

# catalogar(vehiculos, 4)

