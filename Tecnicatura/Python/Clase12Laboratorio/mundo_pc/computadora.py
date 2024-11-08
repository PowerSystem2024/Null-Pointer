from mundo_pc.teclado import Teclado
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f''' 
            {self._nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Tecaldo: {self._teclado}
            Raton: {self._raton}
        '''
    
if __name__ == '__name__':
    teclado1 = Teclado('HP', 'USB')
    monitor1 = Monitor('HP', '17 pulgadas')
    raton1 = Raton('HP', 'USB')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1 )
    print(computadora1)

    teclado2 = Teclado( 'Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', '27 pulgadas')
    raton2 = Raton('Acer', 'Bluetoth')
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2 )
    print(computadora2)

