# Tipo set ---------------
planetas = {'Marte', 'JÚpiter', 'Venus'}
print(len(planetas)) # usamos la funcion len = length significa largo

# Revisar si un elemento existe  dentro de set
print('Júpiter' in planetas)

# Agregar un elemento (ADD)
planetas.add('Tierra') # add una funcion
print(planetas)

# Eliminar elementos , puede arrojar un erros}r si el elemento no existe
# planetas.remove('Júpiter') # esta funcion un mal ingreso u inexistencia del elemento da error
# print(planetas)
planetas.discard('Tierra') # esta funcion no nos presenta ningun error
print(planetas)


#Limpiar set o conjuntos
planetas.clear()
print(planetas)

# Eliminar set
del planetas
# print(planetas) # al eliminar nos muetsra un error

# DICCIONARIO--------------

#'Maradona': 10 Un diccionario sta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario ={
    'IDE': 'Integrated Delopment Environmet',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
print(len(diccionario))
print(diccionario)

# Acceder a un dicconario con la llave(key)
print(diccionario['IDE'])

#  Otra forma de recuperar un elemento 
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificar elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorrer mostrando solo la llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

# Otra maneras de acceder a un diccionario

for termino in diccionario.keys(): 
    print(termino)  # Muestra solo las llaves

for valor in diccionario.values():
    print(valor)   # muestra solo el valor que tiene dentro de la llave
          
# REPASO DE LISTAS Y TUPLAS  