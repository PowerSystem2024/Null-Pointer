
package ejercicio3Clase12;

import java.util.Scanner;


public class Ejercicio3Clase12 {
    
    public static void main (String[]args){
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese la calificacion de participacion (10%): ");
        double participacion = entrada.nextDouble();
        
        System.out.println("Ingrese la calificacion del primer examen parcial (25%): ");
        double parcial1 = entrada.nextDouble();
        
        System.out.println("Ingrese la calificacion del segundo examen parcial (25%): ");
        double parcial2 = entrada.nextDouble();
        
        System.out.println("Ingrese la calificacion del examen final (40%): ");
        double examenFinal = entrada.nextDouble();
        
        double calificacionFinal = participacion * 0.10 + parcial1 * 0.25 + parcial2 * 0.25 + examenFinal * 0.40;
        
        System.out.println("La calificacion Final es: "+calificacionFinal);
   
    }
}
