
package dominio;

public class Persona {
    //Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    private String apellido;
    private double descuentoJubilacion;
    //Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
    // y imprimir , luego modificar sus valores y volver a imprimir

    public Persona(String apellido, double descuentoJubilacion){
    this.apellido = apellido;
    this.descuentoJubilacion = descuentoJubilacion;
    }  

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public double getDescuentoJubilacion() {
        return descuentoJubilacion;
    }

    public void setDescuentoJubilacion(double descuentoJubilacion) {
        this.descuentoJubilacion = descuentoJubilacion;
    }
    
    public String toString(){ //Convierte en una cadena un atributo
        return "Persona [nombre: "+this.nombre+
                ", sueldo: "+this.sueldo+
                ", eliminado: "+this.eliminado+" ]";
    }
}
