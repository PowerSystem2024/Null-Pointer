<<<<<<< HEAD
/*
Uso de la palabra Final
Esta palabra tiene diferentes significativos dependiendo donde se aplique:
        variables: Evita cambiar el valor que almacena la variable
        metodos: Evita que se modifique la definicion o el comportamiento
        de un metodo desde una subclase (Hija)
        clases: Evita que se creen clases hijas
Otra caracteristica es que normalmente,cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una variable
en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cual todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce 
como una constante
*/

=======
>>>>>>> c9b316c1bf2fdf6377a987e41c410fd62361b653
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
<<<<<<< HEAD
        final int miDni = 44008537;
        System.out.println("miDni = " + miDni);
        //miDni = 20312321; no se puede modificar
        //Persona.CONSTANTE_AQUI = 9; // no se modifica
        System.out.println("Mi atributo constante es : "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        
        persona1.setNombre("Ariel Betancud");
        System.out.println("persona1 nombre:  " +persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre:  " +persona1.getNombre());
    }
    
    
=======
        final int miDni = 44247356;
        System.out.println("miDni = " + miDni);
        System.out.println("Mi atributo constante es: "+ Persona.CONSTANTE_AQUI);
        final Persona persona1 = new Persona();
        persona1.setNombre("Juan ignacio Vera");
        System.out.println("persona1 nombre: "+persona1.getNombre() );
        persona1.setNombre("Pepe");
        System.out.println("persona1 nombre: "+persona1.getNombre() );

    }
>>>>>>> c9b316c1bf2fdf6377a987e41c410fd62361b653
}
