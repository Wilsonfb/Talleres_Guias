#Crear una clase CuentaBancaria que represente una cuenta bancaria con atributos 
#de saldo y titular, y métodos para depositar, retirar y consultar el saldo. Además, se 
#deben crear al menos dos objetos de la clase CuentaBancaria y utilizar los 
#métodos creados.
class Cuenta_Bancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo 
        self.titular = titular
    def depositar(self):
        depositar_saldo = self.saldo + depositar
        saldo_total = depositar_saldo
        print(saldo_total)
        return
    def retirar(self):
        retirar_saldo = self.saldo - retirar
        saldo_total_2 = retirar_saldo
        print(saldo_total_2)
        return 
saldo = int(input("Digita el saldo que tiene en la cuenta: "))
titular = input("Digita que titular es: ")
depositador1 = Cuenta_Bancaria (saldo, titular)
depositador2 = Cuenta_Bancaria (120000, "Propietario")
print('''
      1- Depositar
      2- Retirar
      ''')
numero = int(input("Digita lo que quieres hacer en tu cuenta: "))
if numero == 1:
    depositar = int(input("Digita el saldo que quieres depositar: "))
    print(f"Tu saldo en la cuanta es de {depositador1.saldo} y tu titular es de {depositador1.titular}.")
    depositador1.depositar()
    print(f"Tu saldo en la cuanta es de {depositador2.saldo} y tu titular es de {depositador2.titular}.")
    depositador2.depositar()
elif numero == 2:
    retirar = int(input("Digita el saldo que quieres retirar: "))
    print(f"Tu saldo en la cuanta es de {depositador1.saldo} y tu titular es de {depositador1.titular}.")
    depositador1.retirar()
    print(f"Tu saldo en la cuanta es de {depositador2.saldo} y tu titular es de {depositador2.titular}.")
    depositador2.retirar()