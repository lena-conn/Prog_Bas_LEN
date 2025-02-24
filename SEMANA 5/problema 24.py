def suma_serie(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    while True:
        print("\nCálculo de la suma de una serie numérica")
        print("1. Calcular suma de la serie 1 + 2 + ... + n")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            n = int(input("Ingrese el valor de n: "))
            print(f"La suma de la serie hasta {n} es:", suma_serie(n))
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")