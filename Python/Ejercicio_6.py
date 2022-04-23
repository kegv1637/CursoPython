#Pedir un número y decir si es par o impar.
#entradas
num = int(input("Ingrese el numero: "))
#preoceso
resultado = num % 2

if(resultado == 0):
    print("Es PAR")
else:
    print("Es IMPAR")

#salidas