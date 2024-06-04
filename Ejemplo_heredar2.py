class Cepillo:
    def __init__(self, tamaño, color, encias, marca):
        self.tamaño = tamaño 
        self.color  = color
        self.encias = encias
        self.marca = marca
    def especificaciones(self):
        print(f"El cepillo es de color {self.color} tiene un tamaño de {self.tamaño} cm es de encias {self.encias} y la marca que lo hizo es de {self.marca}.")
class Mecanico(Cepillo):
    def __init__(self, tamaño, color, encias, marca, carga, duracion):
        Cepillo.__init__(self, tamaño, color, encias, marca)
        self.carga = carga
        self.duracion = duracion
    def especificaciones_mecanico(self):
        print(f"El cepillo el de la marca {self.marca} es de carga {self.carga} tiene una duracion de carga {self.duracion}.")
cepillo1 = Cepillo(15, "rojo", "delicadas", "colgate")
cepillo1.especificaciones() 
cepillo2 = Mecanico(20, "blanco", "normales", "mecanitro", "lenta", "20 minutos") 
cepillo2.especificaciones()
cepillo2.especificaciones_mecanico()