#Crear una clase llamada Tablas con el atributo número, y un método llamado 
#multiplicar que imprime la tabla de multiplicar deseada por el usuario, el método 
#multiplicar recibe como parámetro el número hasta el cual se desea generar la tabla 
#de multiplicar.
class Tabla:
    def __init__(self, numero):
        self.numero = numero
numero = int(input("Digite el numero de la tabla que quiere ver: "))
print('''
      1.Imprimir la table del 1 al 10.
      2.Imprimir la table del 1 al 50.
      3.Imprimir la table del 1 al 100.
      4.Imprimir la table del 1 al 150.
      5.Imprimir la table del 1 al 200.
    '''  )
menu = int(input("# "))
if menu == 1:
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}.")
elif menu == 2:
    for i in range(1,51):
        print(f"{numero} X {i} = {numero*i}.")
elif menu == 3:
    for i in range(1,101):
        print(f"{numero} X {i} = {numero*i}.")
elif menu == 4:
    for i in range(1,151):
        print(f"{numero} X {i} = {numero*i}.")
elif menu == 5:
    for i in range(1,201):
        print(f"{numero} X {i} = {numero*i}.")
else:
    print("Hubo un error intente nuevamente.")