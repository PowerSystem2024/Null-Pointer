
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;
;


public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        //Tarea
        Producto producto3 = new Producto("Remera", 7200.00);
        Producto producto4 = new Producto("Bermuda", 12500.00);
        Producto producto5 = new Producto("Camisa", 10000.00);
        Producto producto6= new Producto("Lentes", 4600.00);
        Producto producto7= new Producto("Medias", 3700.00);
        Producto producto8= new Producto("Zapatillas", 21000.00);
        Producto producto9=new Producto("Crocs", 20000.00);
        Producto producto10 = new Producto("Gorro", 7200.00);
        Producto producto11 = new Producto("Gorra", 4600.00);
        Producto producto12 = new Producto("Cinturon", 2500.00);
        
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto12);
        orden3.mostrarOrden();
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //Tarea:
        //Crear mas objetos de tipo Producto
        //Crear mas objetos de tipo Orden
    }
    
}
