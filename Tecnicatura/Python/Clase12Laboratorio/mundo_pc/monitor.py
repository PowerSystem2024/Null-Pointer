class Monitor:
    contador_monitores = 0
    

    def __init__(self, marca, tamaño):
        Monitor.contador_monitores += 1
        self._id_monitores = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño
        

    def __str__(self):
        return f'Id: {self._id_monitores}, Mrca: {self._marca}, Tamaño: {self._tamaño} '


if __name__ == '__name__':
    monitor1 = Monitor('HP', '15 Pulgadas')
    print(monitor1)
    monitor2 = Monitor('Acer', '27 pulgadas')
    print(monitor2)
