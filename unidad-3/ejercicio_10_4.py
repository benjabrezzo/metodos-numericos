import numpy as np

# Ejercicio del método numérico para resolver sistemas de ecuaciones lineales, el método se llama descomposicon LU

# n es el número de filas de A
n = 3

# Vamos a pedirle al usario la matriz A
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i][j] = float(input("Ingrese el valor de A[" + str(i) + "][" + str(j) + "]: "))

# Ahora vamos a pedir el vector b que representa a los términos independientes
b = np.zeros(n)
for i in range(n):
    b[i] = float(input("Ingrese el valor de b[" + str(i) + "]: "))

# Iniciamos x en cero, x es un vector de longitud n
x = np.zeros(n)

# Creamos L como la matriz identidad:
L = np.eye(n)

# Copiamos A en U
U = np.copy(A)
# y copiamos x en d
d = np.copy(x)

# descomposición de A en L y U:
for i in range(n):
    for j in range(i+1, n):
        L[j][i] = U[j][i] / U[i][i] # Esto es el coeficiente que se multiplica a la fila i para restarla de la fila j
        for k in range(i, n):
            U[j][k] = U[j][k] - L[j][i]*U[i][k]

# sustitución hacia adelante
d[0] = b[0]
for i in range(1,n):
    d[i] = b[i]
    for j in range(i):
        d[i] = d[i] - L[i][j]*d[j] 
# Es basicamente lo mismo que hicimos con A y U, pero ahora con b y d, utilizando L
        
# Con L pudimos obtener d. Que L la obtuvimos del primer paso descomponiendo A.
# L ya cumplió su función, desde aca no se usa más
        
# Ahora [U] {x} = {d}, que como ya tenemos tanto U como d, podemos resolverlo
# U es una matriz triangular superior, por lo que podemos resolverlo con sustitución hacia atrás, x3 = d3/U33, el primer elemento sale facil. Pero en lugar de 3, usamos n. 
# Y en lugar de n deberiamos usar n-1:
x[n-1] = d[n-1] / U[n-1][n-1]
for i in range(n-2, -1, -1): #-1 no se incluye, va a parar luego del 0
    x[i] = d[i]
    for j in range(i+1, n):
        x[i] = x[i] - U[i][j]*x[j]
    x[i] = x[i] / U[i][i]

#Mostramos A y b origianles:
print("A:")
print(A)

print("b:")
print(b)

#Luego mostramos las matrices L y U que quedaron luego de descomponer A:
print("Las matrices L y U que quedaron luego de descomponer A:")
print("L:")
print(L)
print("U:")
print(U)

print("Con L y b pudimos obtener d:")
print("d:")
print(d)

print("Finalmente, con U y d pudimos obtener x:")
print("x:")
print(x)
        

