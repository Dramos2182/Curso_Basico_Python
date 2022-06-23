#Coleccion sin orden y sin indice

planetas={'Marte','Jupiter','Venus'}
print(planetas)

#Conocer el largo
print(len(planetas))

#Revisar si un elemento esta presente
print('Marte'in planetas)

#Agregar mas elementos
planetas.add("Tierra")
print(planetas)

#NO acepta elementos duplicados
planetas.add('Tierra')
print(planetas)

#Eliminiar elementos
planetas.remove('Tierra')
print(planetas)

planetas.discard('Jupiter')
print(planetas)

#Eliminar todos los elementos
planetas.clear()
print(planetas)

del planetas
print(planetas)