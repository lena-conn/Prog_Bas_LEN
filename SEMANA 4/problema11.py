def es_palindromo(cadena):
   
    cadena = cadena.replace(" ", "").lower()
    
    return cadena == cadena[::-1]

texto = input("Ingrese una palabra o frase: ")
if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
