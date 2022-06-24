

import imp

#Funcion que calcula el total de un pago incluyendo el impuesto
def PagoImpuesto(PagoSinImpuesto, impuesto):
    PagoTotal= PagoSinImpuesto + (PagoSinImpuesto*(impuesto/100))
    return PagoTotal
    


#Ejecucion de la funcion
PagoSinImpuesto = float(input('Ingrese monto sin impuesto: '))
impuesto = float(input('Ingrese monto del impuesto: '))
PagoTotal=PagoImpuesto(PagoSinImpuesto, impuesto)
print (f'El monto final es de: {PagoTotal}')