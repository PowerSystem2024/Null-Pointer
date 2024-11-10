
package caja;

public class PruebaCaja {
    public static void main(String args[]){ //Metodo main
        //Variables locales
        int medidaAncho = 3; //Valores ingresados en codigo duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        CAja caja1 = new CAja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho; //Le pasamos los valores al objeto
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen();//Llamamos al metodo
        //Primer resultado
        System.out.println("Resultado volumen de caja 1: " + resultado);
        
        CAja caja2 = new CAja(2,4,6); //Llamamos al constructor 2 con nuevo argumento
        //LLamamos con el nuevo objeto al metodo para un nuevo calculo
        System.out.println("Resultado volumen de caja2: " + caja2.calcularVolumen());
        
    }
    
    
}
