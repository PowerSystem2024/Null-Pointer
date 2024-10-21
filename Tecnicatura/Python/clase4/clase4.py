import math
import random
from concurrent.futures.process import EXTRA_QUEUED_CALLS

# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.
lista = [1, 2, 3, "Ariel", 7, 7, 3, "Alberto", 1, "Ariel", 2, "Alberto"]
lista = list(set(lista))  # Eliminamos duplicados convirtiendo a set y luego de nuevo a lista
print("Lista sin duplicados:", lista)

# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición):
# 1. lista de palabras que aparecen en las listas
# 2. lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3. lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4. lista de palabras que aparecen en ambas listas
lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)
solo1 = list(conjunto1 - conjunto2)
solo2 = list(conjunto2 - conjunto1)  # Corregido: debería ser conjunto2 - conjunto1
interseccion = list(conjunto1 & conjunto2)

print(f"Lista de elementos que aparecen en ambas listas: {union}")
print(f"Lista de elementos que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de elementos que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de elementos que aparecen en ambas listas: {interseccion}")

# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunadan del norte
# Nombre: Gandalf
# Clase: Mago
# Raza: Istar
# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []

P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P)
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}  # Corregido el nombre
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}  # Corregido 'Aruqero' y 'Raza'
personajes.append(P)
print("Personajes:", personajes)

# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que solo incluya los números menores a 5
# e imprima por consola [1, 3, 2]

lista = [elemento for elemento in tupla if elemento < 5]  # List comprehension
print("Lista de números menores a 5:", lista)

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'Su raíz cuadrada es: {math.sqrt(numero):.2f}')

# Ejercicio 1: Llenar una lista
# Llenar una lista con los números del 1 al 50, luego mostrar
# La lista con el bucle for, los elementos deben mostrarse
# de la siguiente forma: 1-2-3-4-5-...-50
lista = list(range(1, 51))
for i in lista:
    print(i, end='-')
print()  # Nueva línea al final

# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de una lista multiplicándolos por un valor ingresado por el usuario
lista = list(range(1, 11))
print('Lista Original:', end=' ')
for i in lista:
    print(i, end='-')
print()  # Nueva línea al final
valor = int(input('Digite un valor a multiplicar: '))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}:', end=' ')
for i in lista:
    print(i, end='-')
print()  # Nueva línea al final

# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor
lista = []
while True:
    numero = int(input('Digite un número (0 para terminar): '))
    if numero == 0:
        break
    else:
        lista.append(numero)
lista.sort()
print(f'Lista ordenada: \n{lista}')

# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango, por ejemplo:
# suma de números pares del 2 al 30
a = int(input('Digite de dónde va a comenzar la suma: '))
b = int(input('Digite hasta dónde quiere llegar a sumar: '))
suma = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        suma += i
print(f'La suma de números pares dentro del rango es: {suma}')

# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('Error -> El número tiene que ser positivo')
    numero = int(input('Digite un número positivo: '))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f'El factorial del número {numero} es: {factorial}')

# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pide un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo
# si digita el 5, la lista tendrá: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
numero = int(input('Digite un número para su tabla de multiplicar: '))
lista = [i * numero for i in range(1, 11)]  # List comprehension
print(f'Tabla de multiplicar del {numero}: \n{lista}')

for i in lista:
    print(f'{numero} x {lista.index(i) + 1} = {i}')

# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y debe mostrar el número de intentos.
numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input('Adivine el número entre 1 y 100: '))
    intentos += 1
    if intento < numero_aleatorio:
        print('Es mayor')
    elif intento > numero_aleatorio:
        print('Es menor')
    else:
        print(f'¡Felicidades! Adivinaste el número en {intentos} intentos.')
        break

# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones:
# 1. Ingresar dinero en la cuenta
# 2. Retirar dinero de la cuenta
# 3. Mostrar dinero disponible
# 4. Salir

saldo = 1000

while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = input('Digite una opción del menú: ')

    # Validar que la opción sea un número entero
    if not opcion.isdigit():
        print("Por favor, ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion == 1:
        extra = input("¿Cuánto dinero desea ingresar? -> $")

        # Validar que la cantidad sea un número positivo
        if extra.replace('.', '', 1).isdigit() and extra.count('.') <= 1:
            extra = float(extra)
            if extra > 0:
                saldo += extra
                print(f"Dinero en la cuenta al momento: ${saldo:.2f}")
            else:
                print("La cantidad debe ser positiva.")
        else:
            print("Por favor, ingrese una cantidad válida.")

    elif opcion == 2:
        retirar = input("¿Cuánto dinero desea retirar? -> $")

        # Validar que la cantidad sea un número positivo
        if retirar.replace('.', '', 1).isdigit() and retirar.count('.') <= 1:
            retirar = float(retirar)
            if 0 < retirar <= saldo:
                saldo -= retirar
                print(f"Dinero en la cuenta al momento: ${saldo:.2f}")
            elif retirar > saldo:
                print("No tiene suficiente dinero en la cuenta.")
            else:
                print("La cantidad debe ser positiva.")
        else:
            print("Por favor, ingrese una cantidad válida.")

    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: ${saldo:.2f}")

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
        print()

#Ejercicio 9: mostrar una frase sin espacios y contar su longitud
#hacer un programa donde el usuario ingrese una frase, se le
#devolvera la misma frase pero sin espacios en blanco, y
#ademas un contador de cuantos caracteres tiene la frase
#(sin contar los espacios en blanco)
#ejemplo:        frase= vivir por siempre en paz
#                frase final = viviporsiempreenpaz
#                nª de caracteres = 20

frase1 = input("digite una frase")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final:{frase1})
print(f'Nª de caracteres: {len(frase1)}')

