#entradas
nivelAgua = float(input("Nivel de Agua: ")) 
#proceso
if(nivelAgua > 6):
    print("Desbordamiento de Agua en Cisterna")

elif(nivelAgua == 6):
    print("Apagar Bomba")

elif(nivelAgua >= 4 and nivelAgua < 6):
    print("Desacelerar Bomba de Agua")

elif(nivelAgua >= 2 and nivelAgua < 4):
    print("¡Bomba Trabajando!")

elif(nivelAgua > 0 and nivelAgua < 2):
    print("Acelerar Bomba de Agua")

elif(nivelAgua == 0):
    print("Encender Bomba de Agua")

elif( nivelAgua < 0):
    print("Fuga en Cisterna")
