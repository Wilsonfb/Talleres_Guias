class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Automovil(Vehiculo):
    def acelerar(self):
        print("Acelera presionando el pedal del acelerador.")
    def frenar(self):
        print("Frena usando el pedal del freno para que los disco se activen.")
class Motocicleta(Vehiculo):
    def acelerar(self):
        print("Acelera girando el puño del acelerador.")
    def frenar(self):
        print("Frena presionado el freno activando el disco en la rueda delantera y trasera.")
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("Acelera pedaleando.")
    def frenar(self):
        print("Frena presionando las palancas de freno.")
automovil = Automovil()
automovil.acelerar()
automovil.frenar()
motocicleta = Motocicleta()
motocicleta.frenar()
motocicleta.acelerar()
bicicleta = Bicicleta()
bicicleta.acelerar()
bicicleta.frenar()