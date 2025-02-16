print("calculadora de factorial")
numero = int(input("introduzca el numero:"))

factorial = 1

i = 1
while (i <= numero):
        factorial = factorial * i 
        i = i + 1
print ("el factorial de " + str(numero) + " es " + str(factorial))