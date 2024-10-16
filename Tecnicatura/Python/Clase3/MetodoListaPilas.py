# PILAS USANDO LISTAS

pila = [1, 2, 3]

# Agregar elmentos a al pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sancando elementos desde el final
elementoBorrdado = pila.pop() # quita el elemento borrado y lo guarda en la variable
print(f' Sacando el elmento: {elementoBorrdado}')
print(f'La pila ahora quedo asi:  {pila}')
