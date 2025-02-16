def contar_vocales_consonantes(cadena):

    vocales = "aeiouAEIOU"
    vocal_count = 0
    consonant_count = 0
    
    for char in cadena:
        if char.isalpha(): 
            if char in vocales:
                vocal_count += 1
            else:
                consonant_count += 1
    
    return vocal_count, consonant_count

cadena = input("Introduce una cadena de texto: ")
vocales, consonantes = contar_vocales_consonantes(cadena)

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")