#Realizar un programa que conste de una clase llamada Estudiante, que tenga como 
#atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus 
#atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha 
#aprobado o no, además del promedio que obtuvo. Además, se deben crear al menos 
#dos objetos de la clase Estudiante y utilizar los métodos creados.
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def informacion_del_estudiante(self):
        print(f"Nombre del estudiante {self.nombre}.")
        print(f"Nota del estudiante {self.nota}.")
    def aprovado_del_estudiante(self):
        if self.nota <= 33:
            print(f"El estudiante perdio la materia con una nota de {self.nota}.")
        else:
            print(f"El estudiante aprobo con una nota de {self.nota}.")
    def calcular_promedio(estudiantes):
        total_notas = (estudiante1.nota + estudiante2.nota)
        promedio = total_notas / 2
        return promedio
estudiante2 = Estudiante (nombre = "Juanito", nota = 33)
estudiante1 = Estudiante (nombre = "Pepito", nota = 45)
estudiante1.informacion_del_estudiante()
estudiante1.aprovado_del_estudiante()
estudiante2.informacion_del_estudiante()
estudiante2.aprovado_del_estudiante()
estudiantes = [estudiante1, estudiante2]
promedio_total = Estudiante.calcular_promedio(estudiantes)
print(f"El promedio de las notas de los dos estudiantes es {promedio_total}.")