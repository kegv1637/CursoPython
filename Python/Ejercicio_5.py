#Obtener valores para: a, b y c. Calcular la fórmula general.
from cmath import sqrt
#Entradas
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))
#PROCESO

x1 = ((-b) - (pow(((b**2)-(4*a*c)),1/2)))/(2*a)
x2 = ((-b) + (pow(((b**2)-(4*a*c)),1/2)))/(2*a)
#SALIDA

print("El valor de x1 es: ",round(x1,2))
print("El valor de x2 es: ",round(x2,2))
