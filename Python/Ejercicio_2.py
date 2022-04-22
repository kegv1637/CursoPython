# Calcular el área y perímetro de un círculo.
from cmath import pi
#ENTRADAS
valor_radio= int(input("Cual es el radio del circulo: "));
#PROCESOS
area = pi * pow(valor_radio,2);
perimetro = (2*valor_radio)* pi;

#SALIDA
print("El area es igual a :",round(area,2));
print("El perimetro es igual a :",round(perimetro,2));
