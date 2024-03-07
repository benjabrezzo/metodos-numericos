import math
from matplotlib import pyplot as plt

ti = 0.0 #dias
tf = 10.0 #dias
dt = 0.5 #dias
A = 1200.0 #m^2
Q = 500.0 #m^3/dia
alpha = 300

# Creación de un arreglo de para representar el paso del tiempo
n = int((tf-ti)/dt) + 1
t = [0.0]*n
y_num = [0.0]*n

y_num[0] = 0.0

print('    t(dias)     y_num(m)')
print('%8.2f %12.5f' % (t[0], y_num[0]))

for i in range(n-1):
    t[i+1] = t[i] + dt
    y_num[i+1] = y_num[i] + (3*Q/A*(math.sin(t[i+1])**2) - ((alpha*(1+y_num[i])**1.5)/A))*dt
    print ('%8.2f %12.5f' % (t[i+1], y_num[i+1]))

# Graficar la solución numérica
plt.plot(t, y_num,label='Método de Euler',color='b')
plt.legend(loc=2)
plt.show()