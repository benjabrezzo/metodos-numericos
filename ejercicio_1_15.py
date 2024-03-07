from matplotlib import pyplot as plt

ti = 0.0 #minutos
tf = 10.0 #minutos
dt = 0.25 #minutos
# Tasa de evaporación k (mm/h):
k = 0.1 #mm/h
# Al inicio la gota tiene un radio de 3mm
radio = 3.0 #mm
# El área es
A = 4*3.1416*(radio**2) #mm^2
# Por lo tanto el volumen inicial de la gota es:
V = (4/3)*3.1416*(radio**3) #mm^3

# El valor del radio va a ir cambiando en cada iteración
# Por lo tanto, se crea un arreglo para guardar los valores del radio

# El área y el volumen va a ir cambiando con cada iteración con el valor del radio

n = int((tf-ti)/dt) + 1
t = [0.0]*n
V_num = [0.0]*n

# Arreglo para almecenar los valores de radio:
radio_num = [0.0]*n
radio_num[0] = radio

# Arreglo para almacenar los valores de área:
area_num = [0.0]*n
area_num[0] = A


# El valor inicial es:
V_num[0] = V

print('    t(min)     V_num(mm^3)     radio_num(mm)     area_num(mm^2)')
print('%8.2f %12.5f %12.5f %12.5f' % (t[0], V_num[0], radio_num[0], area_num[0]))

for i in range(n-1):
    t[i+1] = t[i] + dt
    V_num[i+1] = V_num[i] - k*area_num[i]*dt

    print('%8.2f %12.5f %12.5f %12.5f' % (t[i+1], V_num[i+1], radio_num[i], area_num[i]))

    # Con el valor del volumen se puede calcular el proximo radio
    radio_num[i+1] = ((3*V_num[i+1])/(4*3.1416))**(1/3)
    #y con esto la proxima area
    area_num[i+1] = 4*3.1416*(radio_num[i+1]**2)

# Si todo funciona bien el radio final debería ser menor a 3mm pues este era el radio inicial y se supone que la gota se evapora.
    


# Graficar la solución numérica
plt.plot(t, V_num,label='Volumen',color='b')
plt.plot(t, radio_num,label='Radio',color='r')
plt.plot(t, area_num,label='Area',color='g')
plt.legend(loc=2)
plt.show()



