# problema del paracaidista
from math import exp
from matplotlib import pyplot as plt # matplotlib es una libreria para graficar
m = 68.1; c = 12.5; g = 9.8
tf = 10.0; ti = 0.0; dt = 0.1  
n = int((tf-ti)/dt) + 1 #n es el numero de elementos en el arreglo t 
t = [0.0]*n; v_num = [0.0]*n; v_an = [0.0]*n #el arreglo t representara los tiempos, por ahora esta lleno de cero, luego se le ira sumando dt.
# v_num es el arreglo que representara la velocidad resuelto por la solución numérica
# v_an es el arreglo que representara la velocidad resuelto por la solución analítica
print('    t(s)     vnum(m/s)    van (m/s)')
print('%8.2f %12.5f %12.5f' % (t[0], v_num[0], v_an[0]))
for i in range(n-1):
    t[i+1] = t[i] + dt
    v_num[i+1] = v_num[i] + (g - c/m*v_num[i])*dt
    v_an[i+1] = g*m/c*(1-exp(-c/m*t[i+1]))
    print ('%8.2f %12.5f %12.5f' % (t[i+1], v_num[i+1], v_an[i+1]))
plt.plot(t, v_num,label='numerica',color='b')
plt.plot(t, v_an,label='analitica',color='g')
plt.legend(loc=2)
plt.show()
