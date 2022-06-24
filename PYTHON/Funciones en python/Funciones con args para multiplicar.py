

def MultiplicarValores(*args):
    resultado1=1
    for valor in args:
        resultado1*=valor
    return resultado1

print(MultiplicarValores(3,5,15))