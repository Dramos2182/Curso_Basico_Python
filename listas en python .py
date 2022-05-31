nombres= [ 'David', 'alma','eduardo','Alo', 'Nancy']
print (nombres)

#Para acceder a un elemento en especifico:
print(nombres[0])
print(nombres[3])

#Accede a los elementos de forma inversa
print(nombres[-1])

#Accede a los elementos dentro del rango
print(nombres[0:2])#no se incluye el 2 
print(nombres[:3])
#Desde el indicado hasta el final
print(nombres[1:])

#Cambiar un valor de la lista
nombres[0]= 'Jonatan'
print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print("Son todos los nombres de la lista")

#Preguntar lo largo de una lista
print(len(nombres))

#Agregar un elemento
nombres.append('David')
print(nombres)

#Agregar un elemento en un indice especifico
nombres.insert(1,"Jorge")
print(nombres)

#Remover un elemento
nombres.remove('Jorge')
print(nombres)

#Remover el ultimo valor agregado
nombres.pop()
print(nombres)

#Eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)

#Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

#Borrar la lista por completo
del nombres
print(nombres)