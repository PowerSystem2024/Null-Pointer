package com.mycompany.ejercicio7;


import java.util.Scanner;


public class Ejercicio7 {

    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       float autos,precio;
       System.out.println("Cuantos autos vendio este mes?");
        autos = entrada.nextFloat();
       System.out.println("A que precio vendio estos autos?");
       precio = entrada.nextFloat();
       
       double salario,comision,carro,salario2;
       salario = 1000;
       comision = autos*150;
       carro = autos *(precio *0.05);
       salario2 = salario+comision+carro;
        System.out.println("El sueldo del empleado es "+salario2);
        
       
       
       
       
       
       
       
        
    }
}
