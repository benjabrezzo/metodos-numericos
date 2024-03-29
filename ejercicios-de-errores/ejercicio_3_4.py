# Ejercicio 3.4

from math import pi


def f(n):
    resultado = 0
    for i in range(1,n+1):
        resultado += 1/i**4
    
    return resultado

def f_inverso(n):
    resultado = 0
    for i in range(n,0,-1):
        resultado += 1/i**4
    
    return resultado


valor_aproximado = pi**4/90

print("Si n=10000 entonces f(n) = ", str(f(10000))+"y el error es ", str(abs(f(10000)-valor_aproximado)*100) + "%")

print("Si n=10000 entonces f_inverso(n) = ", str(f_inverso(10000))+" y el error es ", str(abs(f_inverso(10000)-valor_aproximado)*100) + "%")



