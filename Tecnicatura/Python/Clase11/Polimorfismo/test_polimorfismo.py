from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):  # Este es el método para aprender lo que es el polimorfismo
    # print(objeto) # De manera indirrecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # Esto es para saber el tipo de datos que recibe 
    print(objeto.mostrar_detalles())
    if(isinstance(objeto, Gerente)):
        print(objeto.departamento)




empleado = Empleado('Betsa', 200000)
imprimir_detalles( empleado)

gerente = Gerente('Natalia', 60000, 'Sistemas')
imprimir_detalles(gerente)