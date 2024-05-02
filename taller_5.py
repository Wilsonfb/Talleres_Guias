#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando 
#el método _init_. Calcular después la suma, resta, multiplicación y división. Utilizar 
#un método para cada una e imprimir los resultados obtenidos. Llamar a la clase 
#Calculadora.
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicar = n1 * n2
        self.dividir = n1 / n2
n1 = int(input("Digite el primer numero: "))
n2 = int(input("Digite el segundo numero: "))
operacion = Calculadora(n1, n2)
print(operacion.suma)
print(operacion.resta)
print(operacion.multiplicar)
print(operacion.dividir)