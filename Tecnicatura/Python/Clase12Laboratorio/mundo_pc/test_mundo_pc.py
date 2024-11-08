from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '17 pulgadas')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1 )
print(computadora1)

teclado2 = Teclado( 'Acer', 'Bluetooth')
monitor2 = Monitor('Acer', '27 pulgadas')
raton2 = Raton('Acer', 'Bluetoth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2 )

teclado3 = Teclado('Gamer', 'Bluetooth')
monitor3= Monitor('Gamer', '32 pulgadas')
raton3 = Raton('Gamer', 'Bluetooth')
computadora3= Computadora('Gamer', monitor3, teclado3, raton3)
print(computadora3)

teclado4 = Teclado( 'Apple', 'Bluetooth')
monitor4 = Monitor('Apple', '27 pulgadas')
raton4 = Raton('Apple', 'Bluetoth')
computadora4 = Computadora('Apple', monitor4, teclado4, raton4 )

teclado5 = Teclado( 'Samsung', 'Bluetooth')
monitor5 = Monitor('Samsung', '27 pulgadas')
raton5 = Raton('Samsung', 'Bluetoth')
computadora5 = Computadora('Sansung', monitor5, teclado5, raton5 )
# computadoras mezcladas
computadora6= Computadora('Sansung', monitor1, teclado2, raton4 )
computadora7 = Computadora('Sansung', monitor2, teclado3, raton5)

# Lista
computadoras1 = [computadora1,computadora2,computadora7,computadora4]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)
print(orden1)
# Lista otra
computadoras2 = [computadora3,computadora5, computadora6]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora1)
print(orden2)