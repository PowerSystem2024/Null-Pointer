# Repaso de set o conjunto
# para definir un conjunto 
conjunto2 = set()
conjunto1 = { 'bye', }
conjunto2.add(7)
conjunto2. add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el número 3 NO esta en el conjunto1

# Como hacer igualdad de los conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea  une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #   Que elemento tienene comun
print(conjunto3)
conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1 
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elemento que no comparte o que son diferentes entre ambos
print(conjunto3) 

#REPASO DE DICCIONARIOS

diccionarioNuevo = {'Azul', 'Blue', 'Rojo', 'Red', 'Verde', 'Green', 'Amarrillo', 'Yellow'}
print(diccionarioNuevo)

# Como eliminar 
#del (diccionarioNuevo['Azul'])
# print(diccionarioNuevo)

# Los Diccionario pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83,}, 'Osvaldo': [45, 1.83], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, ' Altura': 1.70, 'Precio': '50 Millones', 'Posición':'Extremo Derecho'},
    11 :{'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posición': 'Extremo Derecho'},
    24 :{'Nombre': 'Paulo Dyvala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19 : {'Nombre ': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1 : {'Nombre': 'FRanco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero' },
    22 : {'Nombre': 'Lautaro Martinez', 'Edad': 27, 'Altura': 1.74, 'Precio': ' 10 Millones', 'Posicion': 'Delantero' },
    9 : {'Nombre': 'Julian Alvarez', 'Edad': 24, 'Altura': 1.70, 'Precio': '8 Millones', 'Posicion': 'Delantero' },
    23 : {'Nombre': 'Emiliano Martinez', 'Edad': 32, 'Altura': 1.90, 'Precio': '25 Millones', 'Posicion': 'Portero' },
    7 : {'Nombre': 'Rodrigo De Paul', 'Edad': 30, 'Altura': 1.89, 'Precio': '11 Millones', 'Posicion': 'Centrocampista' }
}
print(seleccionArgentina[10])

for llave, valor in seleccionArgentina.items(): 
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al dicionario : seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores : ', end=' ' )
print(len(seleccionArgentina)) 