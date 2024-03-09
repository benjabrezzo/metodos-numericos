# Programa para calcular la calificación de un curso que consiste en cuestionarios
# tareas y un examen final.

clave = input("Ingrese la clave del curso: ")
nombre_del_curso = input("Ingrese el nombre del curso: ")
# Peddimos los factores de ponderación para los cuestionario (C), tareas (T) y examen final (E)
C = float(input("Ingrese el factor de ponderación para los cuestionarios: "))
T = float(input("Ingrese el factor de ponderación para las tareas: "))
E = float(input("Ingrese el factor de ponderación para el examen final: "))

n_cuestionarios = int(input("Ingrese el número de cuestionarios: "))
n_tareas = int(input("Ingrese el número de tareas: "))

# En un arreglo vamos a almencar las calificaciones de los cuestionarios
calificaciones_cuestionarios = []
for i in range(n_cuestionarios):
    calificacion = float(input(f"Ingrese la calificación del cuestionario {i+1}: "))
    calificaciones_cuestionarios.append(calificacion)

# Vamos a calcular el promedio ponderado de los cuestionarios
PC = sum(calificaciones_cuestionarios) / n_cuestionarios

# En un arreglo vamos a almencar las calificaciones de las tareas
calificaciones_tareas = []
for i in range(n_tareas):
    calificacion = float(input(f"Ingrese la calificación de la tarea {i+1}: "))
    calificaciones_tareas.append(calificacion)

# Vamos a calcular el promedio ponderado de las tareas
PT = sum(calificaciones_tareas) / n_tareas

# Preguntamos si el curso tiene una calificación final
tiene_examen_final = input("El curso tiene un examen final (s/n): ")

if tiene_examen_final == "s":
    F = float(input("Ingrese la calificación del examen final: "))
    calificacion_final = (C*PC + T*PT + E*F)/(C + T + E)*100
else:
    calificacion_final = (C*PC + T*PT)/(C + T)*100

print(f"La calificación final del curso {nombre_del_curso} con clave {clave} es: {calificacion_final:.2f}")

