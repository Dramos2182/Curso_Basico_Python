
def descendente(numero):
    if numero >=1:
        print(numero)
        descendente(numero-1)
    elif numero==0:
        return
    elif numero <=0:
        print('Valor incorrecto...')


dato =int(input('ingrese un numero: '))
descendente(dato)