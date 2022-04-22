import math

#entradas
grados_c = int(input("Ingrese los grados C: "))
grados_k = int(input("Ingrese los grados K: "))
grados_f = int(input("Ingrese los grados F: "))

#procesos
c_k = grados_c + 273.15
c_f = ((9*grados_c)/5) + 32
k_c = grados_k - 273.15
k_f = ((9*(grados_k - 273.15))/5) + 32
f_c = (5*(grados_f-32))/9
f_k = ((5*(grados_f-32))/9) + 273.15

#salidas

print("Los Grados C a K: ", c_k)
print("Los Grados C a F: ", c_f)
print("Los Grados K a C: ", k_c)
print("Los Grados K a F: ", k_f)
print("Los Grados F a C: ", f_c)
print("Los Grados F a K: ", f_k)

