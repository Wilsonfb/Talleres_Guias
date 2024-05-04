#Crear una clase Estudiante que represente a un estudiante de una escuela. Cada 
#estudiante tendrá un nombre, una lista de lista_de_materias y métodos para agregar una 
#materia, eliminar una materia y calcular el promedio de calificaciones. Además, se 
#deben crear al menos dos objetos de la clase Estudiante y utilizar los métodos 
#creados.
class Estudiante: 
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre 
        self.nota_1 = nota_1 
        self.nota_2 = nota_2 
    def calcular_nota(self):
        nota_final = self.nota_1 + self.nota_2 
        paso_o_no = nota_final / 2
        if paso_o_no <= 35:
            print("Perdio mi chino.")
            print(f"El promedio de sus notas son {paso_o_no}.")
        else:
            print("Usted paso chino.") 
            print(f"El promedio de sus notas son {paso_o_no}.")
def mostrar_materia(materias):
    print("Lista de las materias: ")
    if materias:
        for materia in materias:
            print("-", materia)
    else:
        print()
def buscar_materia(materias, nombre):
    for materia in materias:
        if materia.lower() == nombre.lower():
            return  
materias = []
while True:
    print('''
          1-Agregar maria.
          2-Mostrar lista de las materias.
          3-Eliminar materia.
          4-Salir.
          ''')
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        nombre_materia = input("Ingresar el nombre de la materia: ")
        materias.append(nombre_materia)
        print("Materia agregada.")
    elif opcion == 2:
        mostrar_materia(materias)
    elif opcion == 3:
        materia_eliminar = input("Ingresa el nombre de la materia a eliminar: ")
        if buscar_materia(materias,nombre_materia):
            materias.remove(materia_eliminar)
            print("Eliminado exitosamente.")
        else:
            print("La materia no esta en la lista.")
    elif opcion == 4:
        estudiante1 = Estudiante ("Pepe", 40, 50)
        estudiante2 = Estudiante ("Venito", 30, 20)
        print(f"El nombre del estudiante es {estudiante1.nombre} las notas del estudiante son {estudiante1.nota_1}, {estudiante1.nota_2}.")
        estudiante1.calcular_nota()
        mostrar_materia(materias)
        print("-------------------------------------------------------------------------------------------------------------")
        print(f"El nombre del estudiante es {estudiante2.nombre} las notas del estudiante son {estudiante2.nota_1}, {estudiante2.nota_2}.")
        estudiante2.calcular_nota()
        mostrar_materia(materias)
        break
    else:
        print("Vueleve a intentarlo.")
