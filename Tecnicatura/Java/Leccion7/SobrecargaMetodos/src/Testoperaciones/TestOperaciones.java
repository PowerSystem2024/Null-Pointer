package Testoperaciones;
import Operaciones.operaciones;
public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = operaciones.sumar(7,9);
        System.out.println("resultado = " + resultado);
        var resultado2 = operaciones.sumar(5.0,7);
        System.out.println("resultado2 = " + resultado2);
        var resultado3 = operaciones.sumar(8,6L);
        System.out.println("resultado3 = " + resultado3);
    }
}
