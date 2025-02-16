def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == escala_destino:
        return valor
    
    if escala_origen == "F":
        valor = (valor - 32) * 5/9
    elif escala_origen == "K":
        valor = valor - 273.15
    
    if escala_destino == "F":
        return (valor * 9/5) + 32
    elif escala_destino == "K":
        return valor + 273.15
    elif escala_destino == "C":
        return valor
    else:
        return "Escala no válida"

valor = float(input("Ingrese la temperatura: "))
origen = input("Ingrese la escala de origen (C, F, K): ").upper()
destino = input("Ingrese la escala de destino (C, F, K): ").upper()

resultado = convertir_temperatura(valor, origen, destino)
print(f"La temperatura convertida es: {resultado} {destino}")