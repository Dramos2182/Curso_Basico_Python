from tkinter import EW
from unittest import result


def miFuncion(nombre, apellido):
    print('Saludos desde Mi funcion')
    print(f'Nombre: {nombre} Apelllido: {apellido}')

miFuncion('David', 'Ramos')

def sumar(a=0,b=0):
    return (a+b)

resultado=sumar()
print(f"resultado de sumar: {resultado}")
print(f'Resultado de la suma: {sumar(5,3)}')

