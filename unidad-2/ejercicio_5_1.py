# Método de la bisección
from math import *
def f(x): return -0.5*x**2 + 2.5*x + 4.5
xl = 5; xu = 10; n = 3; i = 0; xr = 0
valor_verdadero = 6.2


while i < n:
    xr_anterior = xr
    xr = (xl + xu)/2
    if f(xl)*f(xr) < 0:
        xu = xr
    else:
        xl = xr
    i += 1
    et = abs((valor_verdadero - xr)/valor_verdadero)*100
    
    if i > 0:
        ea = abs((xr - xr_anterior)/xr)*100

    print(f"Iteración {i}: raíz = {xr:.5f} ea = {ea:.5f} et = {et:.5f}%")

