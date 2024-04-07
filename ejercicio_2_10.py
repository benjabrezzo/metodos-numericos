# Pedimos al usuario el valor de a:
a = float(input("Introduce el valor de a: "))
e = 0
raiz = 0

if a > 0:
    tol = 1e-5
    x = a/2
    while(True):
        y = (x + a/x)/2
        e = abs((y-x)/y)
        x = y
        if e < tol: break
    raiz = x
    print("La raiz cuadrada de "+str(a)+" es: "+str(raiz))
else:
    print("La raiz cuadrada de "+str(a)+" es: "+str(raiz))
