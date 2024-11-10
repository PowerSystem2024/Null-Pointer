
package Ejercicio2Clase11;
import java.util.Scanner;

public class Ejercicio2clase11 {
   
    public static void main(String[]args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la cantidad a pagar: ");
        double compra = Double.parseDouble(entrada.nextLine());
        if(compra > 100){
            double descuento = (compra * 0.2);
            double montofinal = (compra - descuento);
            System.out.println("Se realizo el descuento del 20%");
            System.out.println("El monto final con descuento a pagar es: "+montofinal);
        }
        else{
            System.out.println("No se aplica ningun descuento");
            System.out.println("El monto a pagar es: $"+compra);
        }
        
    }
    
}
    