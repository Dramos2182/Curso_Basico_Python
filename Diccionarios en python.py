diccionario={
'IDE': 'Integrated Development Enviromment',
'OOP': 'Objected Oriented Programming',
'DBMS': 'Database Management System'
}
print(diccionario)

print(len(diccionario))

#Acceder a un elemento (key)
print(diccionario['IDE'])

#Otra fotma de recuperar un elemento
print(diccionario.get('OOP'))

#Modificar elementos
diccionario['IDE']= 'integrated development enviromment'
print(diccionario)

#Recorrer los elementos
for termino,valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#Comprobar existencia de algun elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK']='Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#Limpiar el diccionario
diccionario.clear()
print (diccionario)

#Eliminar el diccionario
del diccionario
print(diccionario)