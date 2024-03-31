# Repaso de como hacer la descomposición LU

import numpy as np

n = input("Ingrese la cantidad de incógnitas: ")
n = int(n)

A = np.zeros((n, n))
b = np.zeros(n)

print("Ingrese la matriz A:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input("Ingrese el valor de A[" + str(i) + "][" + str(j) +"]"))

print("Ingrese el vector b:")
for i in range(n):
    b[i] = float(input("Ingrese el valor de b[" + str(i) + "]: "))

# Iniciamos x en cero, x es un vector de longitud n
x = np.zeros(n)

# Creamos L como la matriz identidad:
L = np.eye(n)

# Copiamos A en U
U = np.copy(A)

for i in range(n):
    for j in range(i+1, n):
        L[j][i] = U[j][i] / U[i][i]
        for k in range(i, n):
            U[j][k] = U[j][k] - L[j][i]*U[i][k]

# Ahora con los mismo factores que se usaron para descomponer A, vamos a descomponer b en d, estos factores están en L:
            
d = np.copy(b)

# d[0] y b[0] son iguales, empezamos desde b[1]
for i in range(1,n):
    for j in range(i):
        d[i] = d[i] - L[i][j]*d[j]

# Ahora con U y d podemos resolver el sistema de ecuaciones lineales:
x[n-1] = d[n-1] / U[n-1][n-1]
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        x[i] = x[i] - U[i][j]*x[j]
    x[i] = x[i] / U[i][i]
