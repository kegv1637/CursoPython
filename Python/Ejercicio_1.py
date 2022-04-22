#Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado

#ENTRADAS
cal_1 = float(input("1era Calificacion: "))
cal_2 = float(input("2da Calificacion: "))
cal_3 = float(input("3era Calificacion: "))

#PRECESOS
promedio = (cal_1+cal_2+cal_3)/3
if(promedio >= 6.0):
    print("La califica es aprobatoria")
else:
    print("La califica es reprobatoria")
#SALIDAS
print("El promedio es de: ",round(promedio,2))

