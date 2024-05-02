#Crear una clase llamada Vehículo con los atributos marca, modelo y color, y un 
#método que defina el precio del vehículo. Luego, crear dos objetos de la clase 
#Vehículo y utilizar el método para establecer el precio de cada uno.
class Vehiculo:
    def __init__(self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo 
        self.color = color
        self.precio = precio
marca = input("Digite la marca del vehiculo: ")
modelo = int(input("Digite el modelo que es el vehiculo: "))
color = input("Digite el color del vehiculo: ")
precio = input("Digite el precio que le quiere dar al segundo vehiculo: ")
vehiculo1 = Vehiculo (marca, modelo, color, precio)
vehiculo2 = Vehiculo ("Toyota", 2020, "Rojo", 300000)
print(f"La marca del vehiculo es {vehiculo1.marca} tiene un color {vehiculo1.color} y es de modelo {vehiculo1.modelo} y tiene un precio de {vehiculo1.precio}.")
print(f"Este vehiculo tiene un color {vehiculo2.color} es de la marca {vehiculo2.marca} y es modelo {vehiculo2.modelo} este vehiculo tiene un precio de {vehiculo2.precio}.")