#Crear una clase llamada Calculadora con una cantidad modificable de atributos que 
#permitan ingresar números y que tenga métodos para sumar, multiplicar, dividir y 
#sacar el promedio, especificando que la cantidad de números a operar se define al 
#crear un objeto de la clase Calculadora.
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.multiplicar = n1 * n2
        self.dividir = n1 / n2
        self.promedio = (n1 + n2) / 2
n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
operacion = Calculadora(n1, n2)
print('''
     1 = suma.
     2 = multiplicar.
     3 = dividir.
     4 = promedio.
      ''')
tipo = int(input("Digite lo que quiere hacer: "))
if tipo == 1:
    print(operacion.suma)
elif tipo == 2:
    print(operacion.multiplicar)
elif tipo == 3:
    print(operacion.dividir)
elif tipo == 4:
    print(operacion.promedio)
else:
    print("Vuelve a intentarlo.")