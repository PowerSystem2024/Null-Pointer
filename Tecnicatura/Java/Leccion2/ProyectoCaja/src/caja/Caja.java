
package caja;// Package


public class CAja { //Clase publica caja
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores (acciones)
    public CAja() { //Constructor 1 = vacio
    } 
    //Constructor con parametros 
    public CAja (int ancho, int alto, int profundo) { //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){ //Metodo para calcular
        return ancho * alto * profundo;
    }
    
}
