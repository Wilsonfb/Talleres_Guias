##Proporciona un ejemplo de polimorfismo en el mundo real y cómo se podría 
##implementar en un sistema orientado a objetos.
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Automovil(Vehiculo):
    def acelerar(self):
        print("El auto celera presionando el pedal del acelerador.")
    def frenar(self):
        print("El auto frena usando el pedal del freno para que los disco se activen.")
class Motocicleta(Vehiculo):
    def acelerar(self):
        print("La moto acelera girando el puño del acelerador.")
    def frenar(self):
        print("La moto frena presionado el freno activando el disco en la rueda delantera y trasera.")
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta acelera pedaleando.")
    def frenar(self):
        print("La bicicleta frena presionando las palancas de freno.")
automovil = Automovil()
automovil.acelerar()
automovil.frenar()
motocicleta = Motocicleta()
motocicleta.frenar()
motocicleta.acelerar()
bicicleta = Bicicleta()
bicicleta.acelerar()
bicicleta.frenar()
