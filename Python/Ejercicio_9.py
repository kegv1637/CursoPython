# Calcular la nómina para un empleado en el mes de Enero del 2022 conociendo
# su pago por día de $250.-

#ENTRADAS
mes = str(input("Mes: "))
dias = int(input("Dias laborales: "))
pago = float(input("Pago por dia: "))
#PROCESO
pago_ba = dias * pago
iva_trs = pago_ba * 0.16
subtotal = pago_ba + iva_trs
iva_ret = (2/3) * iva_trs
isr = pago_ba * 0.10
pago_neto = subtotal - (iva_ret + isr)

#SALIDAS
print("La nomina del mes",mes,"es de: ", round(pago_neto,2))
