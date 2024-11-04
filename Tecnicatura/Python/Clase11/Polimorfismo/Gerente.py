from Empleado import Empleado
# polimormfismoson als diferentes maneras de acceder o usar la imformación o a tarves de diferentes metodo
class Gerente(Empleado):
    def __init__(self,nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

def __str__(self):
    return f'Gerente: [Departamento: {self.departamento} {super().__str__()} ]'