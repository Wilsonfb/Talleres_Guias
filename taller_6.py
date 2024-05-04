#Crear una clase llamada 'Animal' con los atributos nombre, edad y tipo, y mostrar la 
#información del animal, incluyendo su nombre, edad y tipo, es necesario agregar que 
#se deben crear dos objetos de la clase Animal para utilizar los métodos creados.
class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
nombre = input("Digite el nombre del animal: ")
edad = int(input("Digite al edad del animal: "))
tipo = input("Digite el tipo (Raza) del animal: ")
animalito1 = Animal (nombre, edad, tipo)
animalito2 = Animal ("Jorge", 100, "Chiguagua")
print(f"El nombre del animal es {animalito1.nombre} tiene {animalito1.edad} años y es de tipo {animalito1.tipo}.")
print(f"El nombre del animal es {animalito2.nombre} tiene {animalito2.edad} años y es de tipo {animalito2.tipo}.")
