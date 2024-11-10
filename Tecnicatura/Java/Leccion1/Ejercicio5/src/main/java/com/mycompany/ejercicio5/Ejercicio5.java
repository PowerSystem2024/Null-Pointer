
package com.mycompany.ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int calificacionA,calificacionB,calificacionC,suma;
        System.out.println("Digite las 3 Calificaciones");
        calificacionA =entrada.nextInt();
        calificacionB = entrada.nextInt();
        calificacionC = entrada.nextInt();
        suma = calificacionA+calificacionB+calificacionC;
        System.out.println("La suma de las 3 calificaciones es = "+suma );
        
        
        
        
       
        
    }
}
