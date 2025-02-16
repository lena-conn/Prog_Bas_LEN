print("calculadora")

num1 = float(input("introduce el primer numero:"))
num2 = float(input("introduce el segundo numero:"))

operador = input("introduce la operacion que deseas realizar (suma, resta, division o multiplicacion):")

if operador == 'suma':
    resultado = num1 + num2
elif operador == 'resta':
    resultado = num1 - num2
elif operador == 'division':
    resultado = num1 / num2
elif operador == 'multiplicacion':
    resultado = num1 * num2

print ("el resultado es:", resultado)