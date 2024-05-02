#Crear una clase llamada Libro con los siguientes atributos: código, nombre, año y 
#fecha de préstamo. Implementar un método que calcule y muestre la fecha de 
#devolución del libro, considerando que el plazo de préstamo es de 30 días. A 
#continuación, se solicita crear dos objetos de la clase Libro y utilizar el método para 
#visualizar las fechas de devolución correspondientes.
class Libro:
    def __init__(self, codigo, nombre, año, fecha):
        self.codigo = codigo
        self.nombre = nombre 
        self.año = año
        self.fecha = fecha
codigo = int(input("Digita el codigo del libro: ")) 
nombre = input("Digita el nombre del libro: ")
import datetime
fecha = datetime.datetime.now()
date = datetime.date.today()
dias_a_sumar = datetime.timedelta(days=30)
devolucion = fecha + dias_a_sumar
año = date.year
linbro1 = Libro (nombre, codigo)
print(f"El libro se llama {linbro1.nombre}, se registra con el codigo de {linbro1.codigo} y se presta el año de {año}.")
print(fecha.strftime("%Y-%m-%d"))
print(f"La fecha que se debe regresar el libro a la biblioteca es el {devolucion}.")