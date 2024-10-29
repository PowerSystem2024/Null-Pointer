//let persona3 = new Persona ("Carla", "Ponce"); Esto no se debbe hacer

class Persona{ //Clase Padre

    static contadorPersonas = 0; // Atributo estatico
    // email = "Valor default email"; //Atributo no estatico

    static get MAX_0BJ(){ // Este metodo simula una constante
        return 5;
    }

    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_0BJ){
            this.idPersona = Persona.contadorPersonas++;
        }
        else{
            console.log("Se ha superado el maximo de objetos permitidos");
        }
        //console.log("Se incrementa el contador: "+Persona.contadorObjetosPersona);
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this.idPersona+" "+this._nombre+" "+this._apellido;
    }
//Sobreescribiendo el metodo de la clase padre(OBject)
    toString(){ //Regresa un string
        //Se aplica el polimorfismo que signfica = multiples formas en tiempo de ejecucion
        //El metodo que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log("Saludos desde este metodo static");
    }
    static saludar2(persona){
        console.log(persona.nombre+" "+persona.apellido)
    }
}
class Empleado extends Persona{ // Clase hija
    constructor(nombre,apellido,departamento){
        super(nombre, apellido);
        this._departamento = departamento;      
    }

    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }
    //SOBREESCRITURA 
    nombreCompleto(){
        return super.nombreCompleto()+", "+this._departamento;
    }
}
let persona1 = new Persona("Martin", "Perez")
console.log(persona1.nombre);
persona1.nombre ="Juan Carlos";
console.log(persona1.nombre);
persona1.apellido = "Lopez"
console.log(persona1.apellido)
//console.log(persona1);

let persona2 = new Persona("Martina", "Flores")

console.log(persona2.nombre);
persona2.nombre = "Estefania"
console.log(persona2.nombre);
persona2.apellido = "Ramirez"
console.log(persona2.apellido)
//console.log(persona2);

let empleado1 = new Empleado("Maria", "Gimenez", "Sistemas");
console.log(empleado1);
console.log(empleado1.nombre);
console.log(empleado1.nombreCompleto());

// Object.prototype.toString esta es la manera de acceder a atributos y metodos de manera dinamica
console.log(empleado1.toString());
console.log(persona1.toString());
//persona1.saludar(); no se utiliza desde el objeto
Persona.saludar(); 
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

// console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

console.log(persona1.email);
console.log(empleado1.email);
// console.log(Persona.email) No puede acceder desde la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
let persona3 = new Persona("Carla", "Pertosi");
console.log(persona3.toString());
console.log(Persona.contadorPersonas);


console.log(Persona.MAX_0BJ);
// Persona.MAX_0BJ = 10; no se puede modificar ni alterar.
console.log(Persona.MAX_0BJ);

let persona4 = new Persona("Esteban", "Quito");
console.log(persona4.toString());
let persona5 = new Persona("Franco", "Dias");
console.log(Persona.contadorPersonas);
console.log(persona5.toString());

