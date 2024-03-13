from math import *
def f(x): return 5*x**3 - 5*x**2 + 6*x - 2
xl = 0; xu = 1; i = 0; xr = 0; ea = 1
valor_verdadero = 0.32

print("Iteración | xl | xu | xr | f(xl) | f(xu) | f(xr) | ea")
while ea > 10/100:
    xr_anterior = xr
    xr = (xl + xu)/2
    if f(xl)*f(xr) < 0:
        xu = xr
    else:
        xl = xr
    if i > 0:
        ea = abs((xr - xr_anterior)/xr)*100
    print(f"{i} | {xl:.5f} | {xu:.5f} | {xr:.5f} | {f(xl):.5f} | {f(xu):.5f} | {f(xr):.5f} | {ea:.5f}")
    i += 1

    
