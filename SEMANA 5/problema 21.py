import math

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_prisma(base, altura, profundidad):
    return base * altura * profundidad

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio ** 2 * altura

import math

def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_cubo(lado):
    return lado ** 3

def volumen_prisma(base, altura, profundidad):
    return base * altura * profundidad

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio ** 2 * altura

if __name__ == "__main__":
    while True:
        print("\nSeleccione una figura para calcular su área o volumen:")
        print("1. Área de un cuadrado")
        print("2. Área de un rectángulo")
        print("3. Área de un círculo")
        print("4. Área de un triángulo")
        print("5. Volumen de un cubo")
        print("6. Volumen de un prisma")
        print("7. Volumen de una esfera")
        print("8. Volumen de un cilindro")
        print("9. Volumen de un cono")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            print("Área del cuadrado:", area_cuadrado(lado))
        elif opcion == "2":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print("Área del rectángulo:", area_rectangulo(base, altura))
        elif opcion == "3":
            radio = float(input("Ingrese el radio del círculo: "))
            print("Área del círculo:", area_circulo(radio))
        elif opcion == "4":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print("Área del triángulo:", area_triangulo(base, altura))
        elif opcion == "5":
            lado = float(input("Ingrese el lado del cubo: "))
            print("Volumen del cubo:", volumen_cubo(lado))
        elif opcion == "6":
            base = float(input("Ingrese la base del prisma: "))
            altura = float(input("Ingrese la altura del prisma: "))
            profundidad = float(input("Ingrese la profundidad del prisma: "))
            print("Volumen del prisma:", volumen_prisma(base, altura, profundidad))
        elif opcion == "7":
            radio = float(input("Ingrese el radio de la esfera: "))
            print("Volumen de la esfera:", volumen_esfera(radio))
        elif opcion == "8":
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            print("Volumen del cilindro:", volumen_cilindro(radio, altura))
        elif opcion == "9":
            radio = float(input("Ingrese el radio del cono: "))
            altura = float(input("Ingrese la altura del cono: "))
            print("Volumen del cono:", volumen_cono(radio, altura))
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

    
