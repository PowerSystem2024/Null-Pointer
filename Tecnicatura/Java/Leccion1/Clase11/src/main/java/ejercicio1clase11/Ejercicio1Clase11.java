package ejercicio1clase11;

import java.util.Scanner;

public class Ejercicio1Clase11 {
    
    public static void main(String[]args){
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la primer calificacion: ");
        var nota1 = Double.parseDouble(entrada.next());
        System.out.println("Digite la segunda calificacion: ");
        var nota2 = Double.parseDouble(entrada.next());
        System.out.println("Digite la tercer calificacion: ");
        var nota3 = Double.parseDouble(entrada.next());
        double promedio = (nota1 + nota2 + nota3)/3;
        if (promedio >= 70){
            System.out.println("El alumno aprueba el curso con: "+promedio);
        }
        else{
            System.out.println("El alumno desaprueba con: "+promedio);
        }
        
    }
    
}
