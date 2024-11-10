from Producto import Producto
from Orden import Orden

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Vestido', 300.00)
producto4 = Producto('Medias', 50.00)
producto5 = Producto('Blusa', 75.00)
producto6 = Producto('Campera', 250.00)

productos1 = [producto1,producto2]  # LISTA de PRODUCTOS
orden1 = Orden(productos1) # Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}')
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)   # <--metodo de agregarción 
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2 : {orden2.calcular_total()}')
