# Ejercicio para determinar raices de la función f(x) = 2x³ - 11.7x² + 17.7x - 5

# Método Iteración de Punto Fijo

from math import *

def g(x): return (5 + 11.7*x**2 - 2*x**3)/17.7

xv = 3; iter = 0; imax = 3

print("Método Iteración de Punto Fijo:")

while(iter < imax):
    xr = g(xv)
    if(xr != 0):
        ea = abs((xr - xv)/xr) * 100
    iter +=1
    xv = xr
    print("Iteración: ", iter, " xr: ", xr, " ea: ", ea, " %")


print("\n\n")

print("Metodo de Newton-Raphson:")

# Método Newton-Raphson
def f(x): return 2*x**3 - 11.7*x**2 + 17.7*x - 5
def df(x): return 6*x**2 - 23.4*x + 17.7

xv = 3; iter = 0; imax = 3; es = 0.001; ea = 100

while(iter < imax or ea > es):
    xr = xv - f(xv)/df(xv)
    if(xr != 0):
        ea = abs((xr - xv)/xr) * 100
    iter +=1
    xv = xr
    if(iter < imax or ea > es):
        print("Iteración: ", iter, " xr: ", xr, " ea: ", ea, " %")


print("\n\n")

print("Metodo de la Secante:")
# Método de la Secante
def f(x): return 2*x**3 - 11.7*x**2 + 17.7*x - 5

x0 = 3; x1 = 4; iter = 0; imax = 3; 

while(iter < imax):
    x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
    if(x2 != 0):
        ea = abs((x2 - x1)/x2) * 100
    iter +=1
    x0 = x1
    x1 = x2
    print("Iteración: ", iter, " xr: ", x2, " ea: ", ea, " %")