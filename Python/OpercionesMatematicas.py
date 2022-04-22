# Importar una libreria
#libreria de funciones matematicas
import math

# Entradas de Datos
numero_1 = int(input("Escribe el primer numero: "))
numero_2 = int(input("Escribe el segundo numero: "))




# Procesos (calculos u operaciones matematicas y/o Logicas)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
mult = numero_1 * numero_2
div = numero_1 / numero_2

potencia1 = numero_1 ** numero_2
potencia2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)

raiz_Cuadrada1 = pow(numero_1, 1/2)
raiz_Cuadrada2 = math.sqrt(numero_1)
raiz_Cubica = pow(numero_2, 1/3)

#modulo_residuo =


# Salidad de Datos
print ("La suma es igual a", suma)
#print("La suma es igual a " + str(suma))# Concatenacion: Union de textos
#print(f"La suma es igual a {suma}") # f de formateo de textos
print ("La resta es igual a", resta)
print ("La mult es igual a", mult)
print ("La div es igual a", div)

print ("La potencia es igual a", potencia1)
print ("La potencia es igual a", potencia2)
print ("La potencia es igual a", cuadrado)
print ("el cubo es igual a", cubo)

print ("La raiz es igual a", raiz_Cuadrada1)
print ("La raiz es igual a", raiz_Cuadrada2)
print ("La raiz es igual a", raiz_Cubica)
