// Creación de una instancia de Persona
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }

    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }

    // Sobreescribiendo el método de la clase padre (Object)
    toString() {
        return this.nombreCompleto();
    }
}

// Clase Empleado que hereda de Persona
class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento() {
        return this._departamento;
    }

    set departamento(departamento) {
        this._departamento = departamento;
    }

    // Sobreescritura
    nombreCompleto() {
        return super.nombreCompleto() + ', ' + this._departamento;
    }
}

// Creación de instancias y pruebas
let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());

// Acceso dinámico a atributos y métodos con Object.prototype.toString
console.log(empleado1.toString());
console.log(persona1.toString());


