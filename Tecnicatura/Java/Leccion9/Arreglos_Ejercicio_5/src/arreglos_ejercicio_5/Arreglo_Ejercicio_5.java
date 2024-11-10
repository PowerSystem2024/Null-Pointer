/*
Ejercicio 5: Leer por teclado dos tabas de 10 numeros
enteros y mezclarlas en una tercera de la forma: el 1a de A, el 1a de B
el 2 a de A, el 2a de B, etc.
*/
package arreglos_ejercicio_5;

import java.util.Scanner;


public class Arreglo_Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
                int numeros1[] = new int [10];
                int numeros2[] = new int [10];
                int numeros3[] = new int[20];
                
                System.out.println("Llenamos el primero arreglo: ");
                for (int i = 0; i < 10; i++) {
                    System.out.println((i+1)+".Digite un numero: ");
                    numeros1[i] = entrada.nextInt();         
        }
        
                System.out.println("Llenamos el segundo arreglo: ");
                for (int i = 0; i < 10; i++) {
                    System.out.println((i+1) +".Digite un numero: ");
                    numeros2[i] = entrada.nextInt();            
        }
                int j=0;
                for (int i = 0; i < 10; i++) {
                    numeros3[j] = numeros1 [i];
                    j++;
                    numeros3[j] = numeros2 [i];
                    j++;                  
        }
                System.out.println("Mostramos el tercer arrlego: ");
                for (int i = 0; i < 20; i++) {
                    System.out.println(numeros3[i]+" ");                            
        }
                System.out.println();
                
    }
}
