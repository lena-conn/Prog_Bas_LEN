
def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice  
    return -1 

lista = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_lineal(lista, objetivo)
print(f'Índice encontrado en la búsqueda lineal: {resultado}')


def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            bajo = medio + 1  
        else:
            alto = medio - 1  
    return -1  

lista_ordenada = [10, 20, 30, 40, 50]
objetivo = 30
resultado = busqueda_binaria(lista_ordenada, objetivo)
print(f'Índice encontrado en la búsqueda binaria: {resultado}')
