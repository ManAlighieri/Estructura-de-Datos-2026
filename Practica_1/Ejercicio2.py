#Ejercicio 2
cal_alumnos = [8,8,7,5,10,9,9,5,6,10]

promedio_general = sum(cal_alumnos)/len(cal_alumnos)
print(promedio_general)

#Calcular el numero de alumnos aprobados y reprobados
Aprobados = [alumno for alumno in cal_alumnos if alumno >= 6.0]
Aprobado = (len(Aprobados))
Reprobados = [alumno for alumno in cal_alumnos if alumno < 6.0]
Reprobado = (len(Reprobados))
print(Aprobado)
print(Reprobado)

#Calcular el porcentaje de aprobados y reprobados
PorcentajeAprobados = (Aprobado / len(cal_alumnos)) * 100
PorcentajeReprobados = (Reprobado / len(cal_alumnos)) * 100
print(PorcentajeAprobados)
print(PorcentajeReprobados)

#Calcular el numero de alumnos con calificacion mayor a 6.0
Alumno_Mayor = [alumno for alumno in cal_alumnos if alumno >= 6.0]
Num_Alumnos = len(Alumno_Mayor)
print(Num_Alumnos)