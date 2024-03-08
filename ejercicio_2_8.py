# Programa que calcula el valor de coseno usando la serie de Taylor
import math

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos: "))

# Valor verdero (para luego calcular el error)
valor_verdadero = math.cos(x)

# Se esta trabajando en radianes

cos_x = 1 # El primer término de la serie de Taylor es 1
print(f"El valor de cos({x}) con 1 término es: {cos_x}")
valor_porcentual = abs((valor_verdadero - cos_x) / valor_verdadero) * 100
print(f"El error porcentual es: {valor_porcentual:.2f}%")


for i in range(1, n):
    if i % 2 == 0:
        cos_x += x**(2*i) / math.factorial(2*i)
    else: 
        cos_x -= x**(2*i) / math.factorial(2*i)
    print(f"El valor de cos({x}) con {i+1} términos es: {cos_x}")
    valor_porcentual = abs((valor_verdadero - cos_x) / valor_verdadero) * 100
    print(f"El error porcentual es: {valor_porcentual:.2f}%")