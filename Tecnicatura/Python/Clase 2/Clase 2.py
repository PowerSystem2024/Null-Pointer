#tipo set
planetas = {'marte','jupiter','venus'}
print(len(planetas))#Usamos la funcion lean = length significa largo

#Revisar si u elemento existe dentro de set
print('marte'in planetas)

#agregar otro elemento
planetas.add('tierra')
print(planetas)

#eliminar elementos, puede arrojar n error si el elemento no existe
planetas.remove('marte')
print(planetas)
planetas.discard('tierra')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)

#eliminar set o conjunto
del planetas
#print(planetas)

#'maradona':10 un diccionario esta ompuesto de dos elementos
# UNA LLAVE Y UN VALOR
# Dict (key,value)
diccionario = {
    'IDE': 'integrated development environment',
    'POO': 'programacion orientada a objetos',
    'SABD': 'sistema de administracion de base de datos'
}
#verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#otra forma de reuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#modifiamos los elementos
diccionario['IDE'] = 'entorno de desarollo integrado'
print(diccionario)

#como recorrer los elementos
for termino in diccionario:
    print(termino)
#necesitamos una funcion para reorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

#otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino)#muestra solo las llaves

for valor in diccionario.values():
    print(valor)

#comprobar la existencia de algun elemento
print('IDE'in diccionario)

#agregar un elemento
diccionario['PK'] = 'primary key'
print(diccionario)

#eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#vaciar un diccionario
diccionario.clear()
print(diccionario)

#eliminar el diccionario
del diccionario





