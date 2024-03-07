import math

def bhaskara(a, b, c):
    # Dentro de la función primero verificamos si el valor de a es 0
    if a == 0:
        print("El valor de a no puede ser 0")
    else:
        # Si a no es cero pasamos al calcular el discriminante, si es menor a 0 llamamos a la función raices_complejas sino continuamos
        d = (b**2) - (4*a*c)
        if d < 0:
            raices_complejas(a, b, c)
        else:
            # Como el discriminante es mayor o igual a 0, calculamos las raices de la ecuación
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            print(f"Las soluciones de la ecuación son: {x1} y {x2}")

# La función raices_complejas recibe los valores de a, b y c y calcula las raices de la ecuación, solo se llama si el discriminante es negativo.
def raices_complejas(a, b, c):
    d = abs((b**2) - (4*a*c)) # Cuando el discriminante es negativo, se toma el valor absoluto de d y con esto se calculan las raices
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(f"Las soluciones de la ecuación son: {x1}i y {x2}i") # Los valores de raices complejas se imprimen con una i al final


# El programa empieza pidiendo los valores de a, b y c de bhaskara
print("Ingrese el valor de a: ")
a = float(input())
print("Ingrese el valor de b: ")
b = float(input())
print("Ingrese el valor de c: ")
c = float(input())

# Una vez que se tienen los valores de a, b y c, se llama a la función bhaskara
bhaskara(a, b, c)
