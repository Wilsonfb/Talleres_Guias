#Crear una clase Bicicletero con los atributos nombre del usuario, identidad del 
#usuario y tiempo de uso del bicicletero. La clase deberá tener un método para 
#calcular cuánto debe pagar el usuario según el tiempo de uso. Además, se deben 
#crear al menos dos objetos de la clase Bicicletero y utilizar el método creado.
class Bicicletero:
    def __init__(self, nombre_usuario, identificacion, tiempo_uso):
        self.nombre = nombre_usuario
        self.identificacion = identificacion
        self.tiempo = tiempo_uso
    def pago_del_tiempo(self):
        pago = self.tiempo * 200
        print(f"Lo que se debe pagar por el prestamo de la bicicleta es de ${pago:,.2f}.")
        return 
nombre_usuario = input("Nombre de la persona que se le va a prestar la bicicleta: ")
identificacion = int(input("Identificacion del usaurio a prestar: "))
tiempo_uso = int(input("Duracion del prestamo de la bicicle en minutos: "))
persona1 = Bicicletero (nombre_usuario, identificacion, tiempo_uso)
persona2 = Bicicletero ("Wilson", 1032398541, 30)
print(f"El nombre de la persona que se le va a prestar la bicicleta es {persona1.nombre} con la identificacion de {persona1.identificacion} y duro con la bicicleta {persona1.tiempo} minutos.")
persona1.pago_del_tiempo()
print(f"El nombre de la persona que se le va a prestar la bicicleta es {persona2.nombre} con la identificacion de {persona2.identificacion} y duro con la bicicleta {persona2.tiempo} minutos.")
persona2.pago_del_tiempo()