#Una funcion recursiva es una funcion que se llama a si misma 
#para realizar una funcion

def factorial(numero):
    if numero==1:
        return 1
    else :
        return numero*factorial(numero-1)
resultado= factorial(7)
print(f"El factorial de 7 es {resultado}")