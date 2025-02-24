def crear_matriz(filas, columnas):
    print(f"Ingrese los elementos de la matriz {filas}x{columnas} fila por fila:")
    matriz = []
    for i in range(filas):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        while len(fila) != columnas:
            print(f"Debe ingresar exactamente {columnas} valores.")
            fila = list(map(float, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def restar_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    filas_A, columnas_A = len(A), len(A[0])
    filas_B, columnas_B = len(B), len(B[0])
    if columnas_A != filas_B:
        print("Error: El número de columnas de A debe ser igual al número de filas de B.")
        return None
    
    resultado = [[sum(A[i][k] * B[k][j] for k in range(columnas_A)) for j in range(columnas_B)] for i in range(filas_A)]
    return resultado

def transponer_matriz(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

if __name__ == "__main__":
    while True:
        print("\nSeleccione una operación con matrices:")
        print("1. Sumar matrices")
        print("2. Restar matrices")
        print("3. Multiplicar matrices")
        print("4. Transponer matriz")
        print("0. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion in ["1", "2", "3"]:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            print("Matriz A:")
            A = crear_matriz(filas, columnas)
            print("Matriz B:")
            B = crear_matriz(filas, columnas)
            
            if opcion == "1":
                print("Resultado de la suma:")
                imprimir_matriz(sumar_matrices(A, B))
            elif opcion == "2":
                print("Resultado de la resta:")
                imprimir_matriz(restar_matrices(A, B))
            elif opcion == "3":
                print("Resultado de la multiplicación:")
                resultado = multiplicar_matrices(A, B)
                if resultado:
                    imprimir_matriz(resultado)
        elif opcion == "4":
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            print("Matriz A:")
            A = crear_matriz(filas, columnas)
            print("Matriz transpuesta:")
            imprimir_matriz(transponer_matriz(A))
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
