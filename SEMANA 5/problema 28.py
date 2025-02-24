class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.saldo}")
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayor que 0.")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")

def menu_cuenta():
    titular = input("Introduce el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(titular)

    while True:
        print("\nMenú de la Cuenta Bancaria:")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            cantidad = float(input("Introduce la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        
        elif opcion == '2':
            cantidad = float(input("Introduce la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        
        elif opcion == '3':
            cuenta.consultar_saldo()
        
        elif opcion == '4':
            print("Saliendo del sistema bancario...")
            break
        
        else:
            print("Opción no válida. Por favor elige entre 1 y 4.")

menu_cuenta()
