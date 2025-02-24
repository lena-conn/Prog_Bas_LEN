def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {
        "metros": 1,
        "kilometros": 1000,
        "centimetros": 0.01,
        "milimetros": 0.001,
        "pies": 0.3048,
        "yardas": 0.9144,
        "pulgadas": 0.0254
    }

    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        print("Unidades de longitud no válidas.")
        return None

    valor_en_metros = valor * conversiones[unidad_origen]
    valor_convertido = valor_en_metros / conversiones[unidad_destino]
    return valor_convertido


def convertir_masa(valor, unidad_origen, unidad_destino):
    conversiones = {
        "gramos": 1,
        "kilogramos": 1000,
        "toneladas": 1000000,
        "libras": 453.592,
        "onzas": 28.3495
    }

    if unidad_origen not in conversiones or unidad_destino not in conversiones:
        print("Unidades de masa no válidas.")
        return None

    valor_en_gramos = valor * conversiones[unidad_origen]
    valor_convertido = valor_en_gramos / conversiones[unidad_destino]
    return valor_convertido


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsius" and unidad_destino == "fahrenheit":
        return (valor * 9/5) + 32
    elif unidad_origen == "fahrenheit" and unidad_destino == "celsius":
        return (valor - 32) * 5/9
    elif unidad_origen == "celsius" and unidad_destino == "kelvin":
        return valor + 273.15
    elif unidad_origen == "kelvin" and unidad_destino == "celsius":
        return valor - 273.15
    elif unidad_origen == "fahrenheit" and unidad_destino == "kelvin":
        return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "kelvin" and unidad_destino == "fahrenheit":
        return (valor - 273.15) * 9/5 + 32
    else:
        print("Unidades de temperatura no válidas.")
        return None


def menu_conversor():
    print("Bienvenido al Conversor de Unidades")
    
    while True:
        print("\nSeleccione el tipo de conversión:")
        print("1. Longitud")
        print("2. Masa")
        print("3. Temperatura")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            valor = float(input("Introduce el valor a convertir: "))
            unidad_origen = input("Introduce la unidad de origen (metros, kilometros, centimetros, milimetros, pies, yardas, pulgadas): ").lower()
            unidad_destino = input("Introduce la unidad de destino (metros, kilometros, centimetros, milimetros, pies, yardas, pulgadas): ").lower()
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
            if resultado is not None:
                print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}.")
        
        elif opcion == '2':
            valor = float(input("Introduce el valor a convertir: "))
            unidad_origen = input("Introduce la unidad de origen (gramos, kilogramos, toneladas, libras, onzas): ").lower()
            unidad_destino = input("Introduce la unidad de destino (gramos, kilogramos, toneladas, libras, onzas): ").lower()
            resultado = convertir_masa(valor, unidad_origen, unidad_destino)
            if resultado is not None:
                print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}.")
        
        elif opcion == '3':
            valor = float(input("Introduce el valor a convertir: "))
            unidad_origen = input("Introduce la unidad de origen (celsius, fahrenheit, kelvin): ").lower()
            unidad_destino = input("Introduce la unidad de destino (celsius, fahrenheit, kelvin): ").lower()
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
            if resultado is not None:
                print(f"{valor} {unidad_origen} son {resultado} {unidad_destino}.")
        
        elif opcion == '4':
            print("Saliendo del conversor...")
            break
        
        else:
            print("Opción no válida. Por favor elige entre 1 y 4.")


menu_conversor()
