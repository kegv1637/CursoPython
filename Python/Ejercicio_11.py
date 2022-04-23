# Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos
#definir funciones//entrada
def Lista(a, b, c, d,e, f, g, h, i, j):
    return [a, b, c, d,e, f, g, h, i, j]
#proceso
lista_num = Lista(12, 25, 35, 25, 85, 15, 34, 98, 117, 3)
#index            0   1    2   3   4   5   6   7   8   9
#odenar
lista_num.sort()
lista_num.reverse()

#salida
print(f"Lista numerica: {lista_num}")

