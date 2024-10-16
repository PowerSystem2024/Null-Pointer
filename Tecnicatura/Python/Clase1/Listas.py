# lista = Ariel, Liliana, Natalia, Osvaldo

# LAS LISTAS : es lo que se conoce en otros lenguajes como arreglos o vectores 

nombres = ['Naty','Osvaldo', 'Lily', 'Ariel' ]   #dentro de una misma lista pueden haber varios nombres ya sea (tipo strings, numericos,cadenas)
print(nombres)  # con los corchetes podemos buscar uno especifico [0,1...-1]
print(nombres [0:2]) #solo muestra el indice 0, 1 pero no el indice 2

# ir del indice de la lista al indice (sin incluirlo)
print(nombres [ :3]) # Indice a mostrar 0,1,2
# Desde el indice indicando hasta el final
print(nombres [1: ])

# Modificar un valor 
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# Preguntamos cuantos elementos tiene 
print(len(nombres))  # Le pasamos como parametros la lista

# Agregamos un elemento(funcion append le suma en la lista,)
nombres.append('Marcelo') # tipo cadena
nombres.append([1, 2, 3])  #tipo int
nombres.append(True)     # bool
nombres.append(10.45)   # float
nombres.append([4, 5])
nombres.append(7)
print(nombres)      

# Insertar un elemento en un especifico (el orden o posicion)
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')      
print(nombres)

#Eliminamos un elemento(el elementp seleccionado/ especifico)
nombres.remove('Alberto') 
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]  # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar, o limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres) # Aqui nos muestra un error

#REPASO DE LISTAS
# Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6]
lista3 = lista1+lista2  # concatenacion de varias listas
print(lista3)

lista3.extend([7, 8, 9, 1]) # Función para agregar varios elementos a una lista 
print(lista3)

print(lista3.index(5)) # muesatr donde se ubica en que indice esta el valor ingresado0
# print(lista3.index(0)) esto aria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista

print(lista3.count(1))  # cuenta cuantos valores iguales hay dentro de la lista

# Para  poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2 
print(lista3)

# Métodos de Ordenamineto 
lista3.sort()  # ordenar los elementos ascendentemente
print(lista3)
lista3.sort(reverse= True)  # ordena los elementos  descendentemente
print(lista3)