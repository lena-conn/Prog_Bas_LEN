import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

if __name__ == "__main__":
    while True:
        print("\nSeleccione una opción:")
        print("1. Lanzar dado")
        print("2. Lanzar moneda")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            print("El dado cayó en:", lanzar_dado())
        elif opcion == "2":
            print("La moneda cayó en:", lanzar_moneda())
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
