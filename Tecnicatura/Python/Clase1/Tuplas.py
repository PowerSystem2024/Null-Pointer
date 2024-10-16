# Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))  #len(en numeros)

# Acceder a un elemento , para esto utilizamos corchetes no parentesis
print(cocina[0])
# Demostar de manera inversa
print(cocina[-1])

# Accedecer a un rango,  ESTO ES UNA TUPLA
print(cocina[0:2])

# Ejemplo 
verduras = ('papa', )   # Una tupla necesita aunque sea de un elemento: la coma
print(verduras)
# de lo contrario solo seria un tiPo str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina: # Printesat usando \n para saltos de líneas
    print(cocinar, end= '')  # usamos end = para eliminar los saltos de lineas

 # conversion a tupla (no es ,uy recomendada)
cocinalista = list(cocina)
cocinalista[ 0] = 'Plato'
cocina = tuple(cocinalista) 
print('\n', cocina)

#del cocina,   esto es para eliminar una tupla 

#REPASO DE TUPLAS
tupla = (4, 'Hola', 6.78, [1, 2, 3], 4, )  # puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es de tipoo  booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convetir de tuplas a listas y de listas a tuplas
