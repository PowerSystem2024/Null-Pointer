package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 44247356;
        System.out.println("miDni = " + miDni);
        System.out.println("Mi atributo constante es: "+ Persona.CONSTANTE_AQUI);
        final Persona persona1 = new Persona();
        persona1.setNombre("Juan ignacio Vera");
        System.out.println("persona1 nombre: "+persona1.getNombre() );
        persona1.setNombre("Pepe");
        System.out.println("persona1 nombre: "+persona1.getNombre() );

    }
}
