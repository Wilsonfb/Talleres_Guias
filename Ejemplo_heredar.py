##Proporciona un ejemplo de herencia en el mundo real y cómo se podría modelar con 
##clases y objetos.
class Cepillo:
    def __init__(self, tamaño, marca, color):
        self.tamaño = tamaño
        self.marca = marca
        self.color = color
    def cepillo(self):
        print(f"El cepillo mide {self.tamaño} y es de la marca {self.marca}.")
class Normal (Cepillo):
    def __init__(self, tamaño, marca, color, encias):
        Cepillo.__init__(self, tamaño, marca, color)
        self.encias = encias
    def cepi_normal(self):
        print(f"El cepillo es para encias {self.encias}.")
class Mecanico (Cepillo):
    def __init__(self, tamaño, marca, color, carga, duracion):
        Cepillo.__init__(self, tamaño, marca, color)
        self.carga = carga
        self.duracion = duracion
    def meca_cepillo(self):
        print(f"El cepillo es de carga {self.carga} y dura {self.duracion}.")
cepillo1 = Normal("15 cm", "Colgate", "rojo", "suaves")
cepillo1.cepillo()
cepillo1.cepi_normal()
cepillo2 = Mecanico("18 cm", "mecanitro", "blanco", "lenta", "20 minutos")
cepillo2.cepillo()
cepillo2.meca_cepillo()
