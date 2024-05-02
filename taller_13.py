#Crear una clase Libro para representar un libro en una biblioteca. La clase debe 
#tener los siguientes atributos: el título del libro, el autor del libro, el género del libro 
#y un booleano que indica si el libro está disponible para préstamo o no. La clase 
#debe tener el método Imprimir información, que imprimirá el título, autor, género y 
#estado de disponibilidad del libro. Además, se deben crear al menos dos objetos 
#de la clase Libro y utilizar el método Imprimir información.
class Libro:
    def __init__(self, titulo, autor, genero, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible
    def prestar(self):
        if self.disponible:
            print(f"El libro {self.titulo} esta disponible para ser prestado.")
            self.disponible = False
        else:
            print(f"El libro {self.titulo} no esta disponible en estos momentos.")
persona1 = Libro("La Ballena Negra", "Leonardo Dicaprion", "Accion") 
persona2 = Libro("Pinacho", "John Wick", "Drama")
persona1.prestar()
print(f"El libro que me llevo es la {persona1.titulo} es del genero {persona1.genero} y fue escrito por {persona1.autor} gracias.")
print("-----------------------------------------------------------------------------------------------------") 
print("Esta persona quiere el libro de La Ballena Negra.")
persona1.prestar()
print("-----------------------------------------------------------------------------------------------------") 
persona2.prestar() 
print(f"El libro que voy a utilizar es {persona2.titulo} fue escrito por {persona2.autor} y se trata de una historia de {persona2.genero} me lo llevo.")
print("-----------------------------------------------------------------------------------------------------") 
print("Esta persona quiere el libro de Pinacho.")
persona2.prestar() 