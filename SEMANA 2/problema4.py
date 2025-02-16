print("generador de serie fibonacci")
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("indroduce el rango de numeros que deseas para la serie:"))
for i in range(num):
    print(fibonacci(i), end=" ")