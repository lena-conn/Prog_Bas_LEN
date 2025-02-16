def numero_mayor(a, b, c):
    return max(a, b, c)

# Ejemplo de uso
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = numero_mayor(num1, num2, num3)
print(f"El número mayor es: {mayor}")