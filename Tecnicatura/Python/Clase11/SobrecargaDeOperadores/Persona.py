class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre}  {other.nombre}'
    
    def __sub__(self, otro): # Sub significa = substraction (resta)
        return self.edad  - otro.edad

persona1 = Persona('Betsa', 20)
persona2 = Persona('Ali', 14)

# persona1.__add__(persona2), sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)