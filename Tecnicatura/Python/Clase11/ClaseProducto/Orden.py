from Producto import Producto


class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto) # Esto es apara agregar un nuevo producto
    
    def calcular_total(self):
        total = 0 # Variable temporal para almacenar el  total temporal
        for producto in self._productos:
            total +=  producto.precio
        return total
    
    def __str__(self):
        productos_str = ' '
        for producto in self._productos:
            productos_str += producto.__str__()+ '|'
        return f'Orden: {self.id_orden}, \nProducto:{productos_str}'
        
if __name__== '__main__':
    producto1 = Producto('Camiseta', 100.00 )
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1, producto2] # lista de productos
    orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
    print(orden1)
    producto3 = Producto('Vestido', 300.00)
    producto4 = Producto('Medias', 50.00)
    productos2 = [producto3, producto4]
    orden2 = Orden(productos2)
    print(orden2)

# TAREA: Modificar la orden2 ingresando nuevos productos con sus respectivps nombres y precios
# Crear una nueva lista de productos y agregarla a la orden2

