package arreglos_Ejercicio_2;
import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        System.out.println("Guardando los elemementos del arreglo");
        for (int i=0;i<5;i++){
            System.out.print((i+1)+".Digite un numero: ");
            numeros[1] = entrada.nextFloat();

        }
        System.out.println("\n Imprimimos los elementos del arreglo");
        for (int i=4;i>=0;i--){
            System.out.print(i+" "+numeros[i]);
        }
        System.out.println("\n");
    }
}
