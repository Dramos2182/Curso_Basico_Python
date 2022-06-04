#A las tuplas, a diferencia de las listas, ya no se puden modificar
frutas= ('Naranja','Platano', 'Guayaba')
print (frutas)

#Sabar el largo de una tupla
print(len(frutas))


#acceder a un elemento
print(frutas[1])

#Navegacion inversa
print(frutas[-1])

#Acceder a un rango
print(frutas[0:2])

#Recorrer elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ')

#cambiar valor de una tupla
frutasLista=list(frutas)
frutasLista[0]='Pera'
frutas=tuple(frutasLista)
print('\n', frutas)

#eliminar tupla
del frutas