import random

# 1. Distribución uniforme: entre 0 y 1
def distribucion_uniforme():
    return random.uniform(0, 1)

# 2. Distribución normal: media 0 y desviación estándar 1
def distribucion_normal():
    return random.gauss(0, 1)

# 3. Distribución exponencial: lambda = 1
def distribucion_exponencial():
    return random.expovariate(1)

# 4. Distribución binomial: n = 10, p = 0.5
def distribucion_binomial():
    return random.randint(0, 10)  


print("Distribución uniforme:", distribucion_uniforme())
print("Distribución normal:", distribucion_normal())
print("Distribución exponencial:", distribucion_exponencial())
print("Distribución binomial:", distribucion_binomial())