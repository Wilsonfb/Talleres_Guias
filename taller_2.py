#Crear una clase llamada Libro con los siguientes atributos: código, nombre, año y 
#fecha de préstamo. Implementar un método que calcule y muestre la fecha de 
#devolución del libro, considerando que el plazo de préstamo es de 30 días. A 
#continuación, se solicita crear dos objetos de la clase Libro y utilizar el método para 
#visualizar las fechas de devolución correspondientes.
import datetime
class Libro:
    def _init_(self, nombre, codigo, año, fecha):
        self.nombre = nombre 
        self.codigo = codigo
        self.año = año
        self.fecha = fecha
    def calcular_fecha(self):
       dias_a_sumar = datetime.timedelta(days = 30)
       devolucion = self.fecha + dias_a_sumar
       self.año = date.year
       print(f"La fecha de prestamo es {self.fecha.strftime("%Y-%m-%d")}")
       print(f"Lo debe regresar {devolucion}.")
date = datetime.date.today()
nombre = input("Digita el nombre del libro: ")
codigo = int(input("Digita el codigo del libro: "))
linbro1 = Libro(nombre, codigo, date.year, date)
linbro2 = Libro("Las aventuras de piter salchicha", 1032397899, date.year, date) 
print(f"El libro se llama {linbro1.nombre}, se registra con el codigo de {linbro1.codigo} .")
linbro1.calcular_fecha()
print(f"El libro se llama {linbro2.nombre}, se registra con el codigo de {linbro2.codigo} .")
linbro2.calcular_fecha()
