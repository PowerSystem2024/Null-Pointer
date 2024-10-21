#Ejercicio 10: no repetir caracteres
# hacer un programa que pida una cadena por telado, luego
#meter los caracteres en una lista sin repetir caracteres
cadena = input('digite una cadena: ')
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print('f\nLista de caracteres sin repetir ninguno: \n {lista} ')

#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda contactos. crear un
#diccionario donde la clave sea el nombre del usuario y el valor
#sea el telefono, el programa tendra el siguiente menu de opciones:
#    1. nuevo contacto
#    2. borrar contacto
#    3. ver contacto existentes
#    4. salir

agenda = {}
while True:
    print('\t.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú: '))

    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el número de teléfono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Este nombre de contacto ya existe')

    elif opcion == 2:
        nombre = input('¿Cuál es el nombre del contacto?: ')
        if nombre in agenda:
            del agenda[nombre]
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda')

    elif opcion == 3:
        print('Agenda de contactos:')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')

    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break

    else:
        print('Se equivocó de opción de menú')

    print()


#comenzamos con funciones
#mi funcion() no se puede llamar antes de definir a una funcion
#definimos una funcion

def mi_funcion()
    print('Saludos a todos lo alumnos de la Tecnicatura')
mi_funcion()
mi_funcion()

#desempaquetado de listas o list unpackin
def show(name, lastName):
    print(name+ ' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1])
show(*person)
person2 = ("Osvaldo", "Giordanini")
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print('Esto se termino')

#list comprehension, lista de comprension
names = ["Paola", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p [0] == 'p']
print(alongP)

bottlec = [{"name": "Quilmes", "country": "arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella artois", "country": "belgium"},
           ]
arg = [b for b in bottlec if b ["country"] == "Arg"]
print(arg)
print(bottlec)
#paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("saludos a todos lo que ven a traves del anal de youtube")
    print(f'Nombre: {name}, apellido: {lastName}')
    mi_funcion2('Jorge', 'Luero')
    mi_funcion2('Ariel', 'Betancud')
    mi_funcion2('Analia','Pedrosa')

#la palabra return en funciones
#creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0):
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombres)
listarNombres('lucas', 'jose', 'claudia', 'rosa', 'maria')
listarNombres('marcos', 'daniel', 'romina', 'pepe', 'marcela', 'carlos')

#Ejercicio 01: crear una funcion para sumar los valores recibidos de tipo
#numericos, utilizando argumentos variables *arg como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos

def sumar_valor(*args):
    resultado = 0
    # interamos cada elemento
    for valor in args:
        resultado += valor
        return resultado

    #llamamos a la funcion
    print(sumar_valor(3, 5, 9, 2, 1))
    










