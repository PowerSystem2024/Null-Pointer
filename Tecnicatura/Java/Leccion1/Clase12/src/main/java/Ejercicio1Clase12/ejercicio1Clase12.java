
package Ejercicio1Clase12;

import java.util.Scanner;


public class ejercicio1Clase12 {
    public static void main (String[]args){
        Scanner entrada = new Scanner (System.in);
        System.out.println("Digite la cantidad de horas: ");
        int cantidadHoras = Integer.parseInt(entrada.nextLine());
        
        int semanas = cantidadHoras / 168;
        int dias = (cantidadHoras %168)/24;
        int horas = cantidadHoras % 24;
        
        System.out.println("Para"+ cantidadHoras +"horas");
        System.out.println(semanas+"semanas,"+dias+"dias y "+horas +"horas.");
        
    }
    
}
