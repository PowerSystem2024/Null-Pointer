let x = 10;
console.log(x.length);
console.log('Tipos primitivos');

// objeto
let persona = {
    nombre: 'carlos',
    apellido: 'gil',
    email: 'cgil@gmail.com',
    edad: 30,
    idioma: 'es',
    get lang() {
        return this.idioma.toUpperCase();
    },
    set lang(long) {
        this.idioma = long.toUpperCase();
    },
    nombrecompleto: function() { // Error aquí, corregido el "Function()"
        return this.nombre + ' ' + this.apellido;
    },
    get nombreEddad() {
        return 'El nombre es:' + this.nombre + ' Edad: ' + this.edad;
    }
};

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombrecompleto());

let persona2 = new Object();
persona2.nombre = 'juan';
persona2.direccion = 'salada 14';
persona2.telefono = '5492604937389';
console.log(persona2.telefono);

console.log(persona['apellido']);

// for in
for (propiedad in persona) {
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('cambiamos y eliminamos un error');
persona.apellido = 'torres';
delete persona.apellido;
console.log(persona);

// distinta forma de imprimir un objeto
// numero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('distinta forma de imprimir un objeto: forma');
console.log(persona.nombre + ' , ' + persona.apellido);

// numero 2: a traves del ciclo for in
for (nombrepropiedad in persona) {
    console.log(persona[nombrepropiedad]);
}

// nombre 3: la funion object.values()
let personaArray = Object.values(persona);
console.log('distinta forma de imprimir un objeto: forma 3');
console.log(personaArray);

// numero 4: utilizaremos el metodo JSON.stringify
console.log('distinta forma de imprimir un objeto: forma 4');
let personastring = JSON.stringify(persona); // Error aquí, corregido "json" a "JSON"
console.log(personastring);

console.log('comenzamos a utilizar el metodo get');
console.log(persona.nombreEddad);

console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function persona3(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombrecompleto = function() {
        return this.nombre + ' ' + this.apellido;
    };
}
let padre = new persona3('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis';
padre.telefono = '3849298849';
console.log(padre);
console.log(padre.nombrecompleto());
let madre = new persona3('Laura', 'contrera', 'Contreral@gmail.com');
console.log(madre);
console.log(madre.nombrecompleto());

// diferentes formas de crear objetos
// caso numero 1
let miObjeto = new Object();
// caso numero 2
let miObjeto2 = {};

// caso string 1
let micadena1 = new String('Hola');
// caso string 2
let micadena2 = 'Hola';

// caso numero 1
let miNumero = new Number(1);
// caso numero 2
let miNumero2 = 1;

// caso boolean 1
let miboolean1 = new Boolean(false);
// caso boolean 2
let miBolean2 = false;

// caso Arreglo 1
let miArreglo1 = new Array();
// caso Arreglo 2
let miArreglo2 = [];

// caso funcion 1
let miFuncion = new function() {};
// caso funcion 2
let miFuncion2 = function() {};

// uso de prototype
persona3.prototype.telefono = '3604829345';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '888374738';
console.log(madre.telefono);

// uso de call
let persona4 = {
    nombre: 'juan',
    apellido: 'perez',
    nombrecompleto: function(titulo, telefono) {
        return titulo + ': ' + this.nombre + ' ' + telefono;
        // return this.nombre + ' ' + this.apellido;
    }
};

let persona5 = {
    nombre: 'carlos',
    apellido: 'lara',
};

console.log(persona4.nombrecompleto('Lic.', '833992784'));
console.log(persona4.nombrecompleto.call(persona5, 'ing.', '83948849493'));

// metodo apply
let arreglo = ['ing', '833994098774'];
console.log(persona4.nombrecompleto.apply(persona5, arreglo));




