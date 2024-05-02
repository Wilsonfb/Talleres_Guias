#Crear una clase Película con los atributos título, fecha de estreno, duración en 
#minutos y género. La clase deberá tener métodos para mostrar la información de la 
#película, calcular la duración en horas y determinar si es una película de acción. 
#Además, se deben crear al menos dos objetos de la clase Película y utilizar los 
#métodos creados.
class Pelicula:
    def __init__(self, titulo, fecha_estreno, duracion, genero):
        self.titulo = titulo
        self.fecha_estreno = fecha_estreno
        self.duracion = duracion
        self.genero = genero
    def calcura_horas(self):
        if self.duracion >= 60 >= 119:
            print("La duracion de la pelicula es 1 hora o mayor.")
        elif self.duracion >= 120 >= 180:
            print("La duracion de la pelicula es de 2 horas o mayor.")
        elif self.duracion <= 59:
            print("La pelicula dura menos de 1 hora.")
        else:
            print("La duracion de la pelicula es mayor a 3 horas.")
titulo = input("Digite el nombre de la pelicula: ")
duracion = int(input("Digite la duracion de la pelicula en minutos: ")) 
fecha_estreno = int(input("Digite la fecha de la pelicula: ")) 
genero = input("Digite el genero de la pelicula: ")
pelicula1 = Pelicula (titulo, fecha_estreno, duracion, genero)
pelicula2 = Pelicula ("Pinocho", 2004, 130, "animacion")
print(f"La pelicula se llama {pelicula1.titulo} es de genero {pelicula1.genero} se estreno el año de {pelicula1.fecha_estreno}.")
pelicula1.calcura_horas()
print(f"La pelicula se llama {pelicula2.titulo} es de genero {pelicula2.genero} se estreno el año de {pelicula2.fecha_estreno}.")
pelicula2.calcura_horas()