#Definimos nuestra funcion de sumar valores
def SumarValores(*args):
    resultado=0
    #Iteramos cada elemento de los argumentos variables
    for valor in args:
        #Resultado = resultado + valor
        resultado+=valor
    return resultado

#LLamada a nuestra funcion
print(SumarValores(3,5,9))