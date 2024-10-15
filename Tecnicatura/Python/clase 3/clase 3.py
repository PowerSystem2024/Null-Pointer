#para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)

#como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)

#operaciones en conjunto
conjunto3 = conjunto1 | conjunto2
print(conjunto3)
conjunto3 = conjunto1 & conjunto2
print(conjunto3)

conjunto3 = conjunto1 - conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset

#ejercicio con diccionario
seleccionargentina = {
    10:{'nombre':'lionel messi','edad': 35,'altura': 1.70,'precio': '50 millones', 'Posicion':'extremo derecho'}
    11:{'nombre':'angel di maria', 'edad':34,'altura': 1.80, 'precio':'12 millones','posicion':'extremo dereho'}
    24:{'nombre':'pablo dybala','edad': 28,'altura': 1.77,'precio': '35 millones','posicion':'media punto'}
    19:{'nombre':'nicolas otamendi', 'edad':34,'altura': 1.83,'precio':'3.5 millones','posicion':'defensa central'}
    1:{'nombre':'franco armani','edad': 35,'altura': 1.89,'preio':'3.5 millones','posicion':'portero'}
    23:{'nombre':'emiliano martinez','edad': 32,'altura': 1.95,'precio': '28 millones', 'Posicion':'portero'}
    13:{'nombre':'cristiano romero','edad': 26,'altura': 1.85,'precio': '65 millones', 'Posicion':'defensa central'}
     9:{'nombre':'julian alvarez','edad': 23,'altura': 1.70,'precio': '60 millones', 'Posicion':'delantero'}
    24:{'nombre':'enzo fernandez','edad': 23,'altura': 1.78,'precio': ' 75 millones', 'Posicion':'medio centro'}
}
for llave,valor in seleccionargentina.items():
    print(llave,valor)







