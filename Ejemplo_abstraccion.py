##Proporciona un ejemplo de abstracción en el mundo real y cómo se podría 
##representar mediante clases y objetos.
class Conocido:
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apelldio = apellido
    def saludar(self):
        print(f"Hola {self.nombre} {self.apelldio} como te encuentras el dia de hoy.")
    def ignorar1(self):
        print(f"....................")
class Desconocido(Conocido):
    def __init__ (self, nombre, apellido, estudio):
        Conocido.__init__(self, nombre, apellido)
        self.estudio = estudio
    def presentarse(self):
        print(f"Hola mucho gusto me presento mi nombre es {self.nombre} y mi apellido es {self.apelldio} y estudio {self.estudio}.")
    def ignorar2(self):
        print(f"....................")
persona1 = Conocido("Nixson", "Rodriguez")
persona2 = Desconocido("Nixson", "Rodriguez", "Matematicas")
while True:
    print('''
        Conocido.
        Desconocido.
        Salir.  
          ''')
    personita = input("DESICION + ")
    if personita == "conocido":
        while True:
            print('''
                Saludar.
                Ignorar.
                Salir.  
                  ''')
            desicion = input("CONOCIDO + ")
            if desicion == "saludar":
                persona1.saludar()
            elif desicion == "ignorar":
                persona1.ignorar1()
            elif desicion == "salir":
                break
            else:
                print("ERROR")
    elif personita == "desconocido":
        while True:
            print('''
                Presentarse.
                Ignorar.
                Salir.  
                  ''')
            desicion = input("DESCONOCIDO + ")
            if desicion == "presentarse":
                persona2.saludar()
            elif desicion == "ignorar":
                persona2.ignorar2()
            elif desicion == "salir":
                break
            else:
                print("ERROR")
    elif personita == "salir":
        print("Se va sin hacer nada.")
        break
    else:
        print("ERROR")