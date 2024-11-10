<<<<<<< HEAD

=======
>>>>>>> c9b316c1bf2fdf6377a987e41c410fd62361b653
package domain;

public class Persona {
    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
<<<<<<< HEAD
        return this.nombre;
=======
        return nombre;
>>>>>>> c9b316c1bf2fdf6377a987e41c410fd62361b653
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

<<<<<<< HEAD
    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}'+" ,"+super.toString();
    }
    
    
    
=======

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Persona{");
        sb.append("nombre='").append(nombre).append('\'');
        sb.append('}');
        return "Persona{" + "nombre=" + nombre + '}' + ", "+super.toString();
    }
>>>>>>> c9b316c1bf2fdf6377a987e41c410fd62361b653
}
