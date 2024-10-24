//numero 4 : utilizaremos el metodo JSON.stringify
console.log('distinta forma de imprimir un objeto: forma 4');
let personastring = json.stringify(persona);
console.log(personastring);

console.log('comenzamos a utilizar el metodo get');
console.log(persona.nombreEddad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombrecompleto = function(){
        return this.nombre+ ' '+this.apellido;
    }
}
let padre = new persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';
padre.telefono = '3849298849';
console.log(padre);
console.log(padre.nombrecompleto());
let madre = new persona3('Laura', 'contrera', 'Contreral@gmail.com');
console.log(madre);
console.log(madre.nombrecompleto());

//diferentes formas de crear objetos
//caso numero 1
let miObjeto = new Object();
//caso numero 2
let miObjeto2 = {};

//caso string 1
let micadena1 = new String('Hola');
//caso string 2
let micadena2 = 'Hola';

//caso numero 1
let miNumero = new Number(1);
//caso numero 2
let miNumero2 = 1;

//caso boolean 1
let miboolean1 = new Boolean(false);
//caso boolean 2
let miBolean2 = false;

//caso Arreglo 1
let miArreglo1 = new Array();
//caso Arreglo 2
let miArreglo2 = [];

//caso funcion 1
let miFuncion = new function(){};
//caso funcion 2
let miFuncion2 = function(){};

//uso de prototype
persona3.prototype.telefono = '3604829345';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '888374738';
console.log(madre.telefono);

//uso de call
let persona4 = {
    nombre: 'juan',
    apellido: 'perez',
    nombrecompleto: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'carlos',
    apellido: 'lara',
}

console.log(persona4.nombrecompleto2('Lic.', '833992784'));
console.log(persona4.nombrecompleto2.call(persona5, 'ing.', '83948849493'));

//metodo apply
let arreglo = ['ing', '833994098774'];
console.log(persona4.nombrecompleto2.apply(persona5, arreglo));