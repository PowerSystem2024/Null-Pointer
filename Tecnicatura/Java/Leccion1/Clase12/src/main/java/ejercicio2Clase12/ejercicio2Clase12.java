
package ejercicio2Clase12;

import java.util.Scanner;

public class ejercicio2Clase12 {
    
    public static void main (String[]args){
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese el valor de a: ");
        double a = entrada.nextDouble();
        
        System.out.println("Ingrese el valor de b: ");
        double b = entrada.nextDouble();
        
        double resultado1 = Math.pow(a + b,2);
        double resultado2 = Math.pow(a,2) + Math.pow(b,2)+2*a*b;
        
        System.out.println("Resultado usando la formula (a+b)^2= a^2 + b^2 + 2ab: "+resultado1);
        System.out.println("Resultado calculado directamente: a^2 + b^2 + 2ab: "+resultado2);
        
    }
    
}
