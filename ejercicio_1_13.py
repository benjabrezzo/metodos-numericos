import math #Para usar la función de seno
from matplotlib import pyplot as plt # matplotlib es una libreria para graficar

ti = 0.0 #dias
tf = 10.0 #dias
dt = 0.5 #dias
A = 1200.0 #m^2
Q = 500.0 #m^3/dia

# Creación de un arreglo de para representar el paso del tiempo
n = int((tf-ti)/dt) + 1 #n es el numero de elementos en el arreglo t, el + 1 es porque el rango de la funcion range(n) es de 0 a n-1
t = [0.0]*n #el arreglo t representara los tiempos, por ahora esta lleno de cero, luego se le ira sumando dt.
y_num = [0.0]*n #el arreglo y_num representara la profundidad del agua resuelto por la solución numérica

y_num[0] = 0.0 #m, la profundidad del agua en el tiempo t = 0 es 0

print('    t(dias)     y_num(m)')
print('%8.2f %12.5f' % (t[0], y_num[0]))

for i in range(n-1):
    t[i+1] = t[i] + dt #se le suma el paso de tiempo al tiempo anterior
    y_num[i+1] = y_num[i] + (3*Q/A*(math.sin(t[i+1])**2) - Q/A)*dt #se calcula la profundidad del agua en el tiempo t[i+1] usando la solución numérica
    print ('%8.2f %12.5f' % (t[i+1], y_num[i+1])) #se imprime el tiempo y la profundidad del agua en el tiempo t[i+1]

# Graficar la solución numérica
plt.plot(t, y_num,label='Método de Euler',color='b')
plt.legend(loc=2) #loc=2 es la posición de la leyenda en la gráfica
plt.show() #muestra la gráfica