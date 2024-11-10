/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y de cada columna
*/
package matrices_ejercicio_5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matrices_ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][],nFilas,nCol,sumarFilas,sumarCol;
        int posFila,posCol;
        
        nFilas= Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: ")); 
        nCol=Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: "));
        
        matriz = new int[nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int [nCol];
        
        System.out.println("Rellenando la matriz: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.println("Matriz["+i+"]["+j+"]");
                matriz[i][j] = entrada.nextInt();               
            }            
        }
        System.out.println("\nMatriz Original: ");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.println(matriz[i][j]+" ");               
            }
            System.out.println("");           
        }
        System.out.println(""); 
        //Sumando las filas
        posFila=0;
        for (int i = 0; i < nFilas; i++) {
            sumarFilas = 0;
            for (int j = 0; j < nCol; j++) {
                sumarFilas += matriz[i][j];      
            }
            filas[posFila] =sumarFilas;
            posFila++;               
            }
        //Sumando las columnas
        posCol=0;
        for (int i = 0; i < nCol; i++) {
            sumarCol = 0;
            for (int j = 0; j < nFilas; j++) {
                sumarCol += matriz[i][j];    
            }  
            columnas[posCol] = sumarCol;
            posCol++;
        }
        System.out.println("\nLa suma de las filas es: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.println(filas[i]+" - ");            
        }
        System.out.println("");
        
        System.out.println("\nLa suma de las columnas es: ");
        for (int i = 0; i < nCol; i++) {
            System.out.println(columnas[i]+" - ");                    
        }
        System.out.println("");
            
        }
    }
   
