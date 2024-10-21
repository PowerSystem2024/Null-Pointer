class persona:  # Creamos una clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'persona: {self.nombre} {self.apellido}, {self.edad}')  # Corregido el paréntesis

persona1 = persona('Ariel', 'Betancud', 40)
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre}, {persona1.apellido}, su edad es: {persona1.edad}')

persona2 = persona('Osvaldo', 'Glordanini', 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}')  # Corregido el paréntesis

# persona2 = persona('Ariel', 'Betancud', 40)  # Esta línea es redundante
#print(f'El objeto1 de la clase persona:){persona1.nombre} {persona1.apellido} su edad es: {persona1.edad }')

persona1.nombre = 'Sofia'
persona1.apellido = 'Torres'
persona1.edad = 19
print(f'El objeto1 modificado de la clase persona: {persona1.nombre}, {persona1.apellido}, su edad es: {persona1.edad}')

# Los atributos son: características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()


