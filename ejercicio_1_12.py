from math import exp
from matplotlib import pyplot as plt

tf = 10.0 #dias
ti = 0.0 #dias 
dt = 0.1 #dias
k = 0.2 #dias^-1

# Creación de un arreglo de para representar el paso del tiempo
n = int((tf-ti)/dt) + 1 #n es el numero de elementos en el arreglo t, el + 1 es porque el rango de la funcion range(n) es de 0 a n-1
t = [0.0]*n #el arreglo t representara los tiempos, por ahora esta lleno de cero, luego se le ira sumando dt.
c_num = [0.0]*n #el arreglo v_num representara la concentración del contaminante resuelto por la solución numérica

# En el tiempo t = 0, la concentración del contaminante es c = 10Bq/L
c_num[0] = 10.0 #Bq/L

print('    t(dias)     c_num(Bq/L)')
print('%8.2f %12.5f' % (t[0], c_num[0]))

for i in range(n-1):
    t[i+1] = t[i] + dt #se le suma el paso de tiempo al tiempo anterior
    c_num[i+1] = c_num[i] - k*c_num[i]*dt #se calcula la concentración del contaminante en el tiempo t[i+1] usando la solución numérica
    print ('%8.2f %12.5f' % (t[i+1], c_num[i+1])) #se imprime el tiempo y la concentración del contaminante en el tiempo t[i+1]

# Graficar la solución numérica
plt.plot(t, c_num,label='Método de Euler',color='b')
plt.legend(loc=2) #loc=2 es la posición de la leyenda en la gráfica
plt.show() #muestra la gráfica