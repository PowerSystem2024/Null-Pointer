miFuncion(8, 2); // Esto se le conoce como hoisting

function miFuncion(a, b) {
    // console.log("sumamos: "+ (a + b)); // Sumamos: 10
    return a + b;
}

// Llamamos la función
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado); // 13

// Declaramos una función de tipo expresión o anónima
let x = function(a, b) { return a + b; }; // necesita cierre con punto y coma
resultado = x(5, 6); // al llamarla se pone la variable y paréntesis
console.log(resultado); // 11

// Funciones de tipo self-invoking
(function(a, b) {
    console.log('Ejecutando la función: ' + (a + b));
})(9, 6); // Corregido el nombre de la función y paréntesis

// Verificando el tipo de la función
console.log(typeof miFuncion); // function

function miFuncion(a, b) {
    console.log(arguments); // Muestra todos los argumentos
}

miFuncion(5, 7, 3, 6); // Pasa más de dos parámetros

// toString
function miFuncionDos() {
    return 'Ejemplo';
}
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); // Muestra el código de la función

// Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); // Asignamos el valor a una variable
console.log(resultado); // 10

// Función tipo expresión
let sumar = function(a = 4, b = 8) {
    console.log(arguments[0]); // muestra el parámetro de: a (3)
    console.log(arguments[1]); // muestra el parámetro de b: (2)
    return a + b + arguments[2]; 
};
resultado = sumar(3, 2, 9); 
console.log(resultado); // 14

// Sumar todos los argumentos
function sumarTodos() {
    let suma = 0;
    for (let i = 0; i < arguments.length; i++) {
        suma += arguments[i]; // arguments es para arreglos
    }
    return suma;
}
let respuesta = sumarTodos(5, 4, 13, 10, 9);
console.log(respuesta); // 41

// Tipos primitivos
let k = 10; // Definir la variable
function cambiarValor(a) { // paso por valor
    a = 20;
}
cambiarValor(k);
console.log(k); // Sigue siendo 10, porque es por valor

// Objetos (paso por referencia)
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez' // Corregir coma faltante
};

function cambiarValorObjeto(p1) {
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez'; // Corregido el nombre de la propiedad
}

cambiarValorObjeto(persona);
console.log(persona); // {nombre: 'Ignacio', apellido: 'Perez'}
