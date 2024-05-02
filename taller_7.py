#Crear una clase llamada 'Empresa' que gestione la información de los empleados, 
#incluyendo el nombre del empleado, los días trabajados, el salario de la persona y la 
#nómina total de la empresa. Cada día de trabajo equivale a $40,000. Se deben crear 
#dos objetos de la clase Empresa para utilizar los métodos creados. Mostrar el nombre 
#del empleado junto a los días trabajados y al salario de esa persona. Finalmente, 
#mostrar la nómina total de la empresa."
class Empresa:
    def __init__(self, nombre, dias):
        self.nombre = nombre
        self.dias = dias
        self.salario_diario = 40000
    def calcular_salario(self):
        return self.dias * self.salario_diario
empleado1 = Empresa("Cristiano", 20)
empleado2 = Empresa("Falcao", 25)
print(f"Empleado 1 {empleado1.nombre} los días trabajados son {empleado1.dias} y el salario final es de ${empleado1.calcular_salario():,.2f}.")
print(f"Empleado 2 {empleado2.nombre} los días trabajados son {empleado2.dias} y el salario final es de ${empleado2.calcular_salario():,.2f}.")
print(f"La nomina total de la empresa es de ${empleado1.calcular_salario() + empleado2.calcular_salario():,.2f}")