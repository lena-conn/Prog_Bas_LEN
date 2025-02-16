import cmath  

def resolver_ecuacion_cuadratica(a, b, c):
    
    discriminante = b**2 - 4*a*c
    
    
    sol1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    sol2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
    
    return sol1, sol2


a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

soluciones = resolver_ecuacion_cuadratica(a, b, c)

print(f"Las soluciones de la ecuación son: {soluciones[0]} y {soluciones[1]}")