
package Ejercicio3Clase11;

import java.util.Scanner;


public class Ejercicio3Clase11 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite el primer numero: ");
        double numero1 = Double.parseDouble(entrada.nextLine());
        System.out.println("Digite el segundo numero: ");
        double numero2 = Double.parseDouble (entrada.nextLine());
        if (numero1 == numero2){
            double resultado = numero1 * numero2;
            System.out.println("Se multiplican los dos numeros"+resultado);
        }
        else if(numero1 > numero2){
            double resultado = numero1 - numero2;
            System.out.println("Si el primer numero es mayor que el segundo se restan"+resultado);
        }
        else{
            double resultado = numero1 + numero2;
            System.out.println("Si el primer numero es menor que el segundo se suman: "+resultado);
            
        
        }
        
      
    }
    
}
