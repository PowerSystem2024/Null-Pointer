// let autos = new Array("Ferrari", "Renault", "BMW"); esta es la sintaxis vieja
const autos = ["Ferrari", "Renault", "BMW"];
console.log(autos); // ["Ferrari", "Renault", "BMW"]

// Recorremos los elementos de un arreglo
console.log(autos[0]); // Ferrari
console.log(autos[2]); // BMW

for (let i = 0; i < autos.length; i++) {
    console.log(i + ' : ' + autos[i]);
}

// Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]); // Volvo

// Agregamos nuevos valores al arreglo
autos.push('Audi'); // Agregamos el elemento al final del arreglo
console.log(autos); // ["Ferrari", "Volvo", "BMW", "Audi"]

// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porsche';
console.log(autos); // ["Ferrari", "Volvo", "BMW", "Audi", "Porsche"]

// Tercera forma de agregar elementos teniendo CUIDADO
autos[50] = "Renault";
console.log(autos); 
// ["Ferrari", "Volvo", "BMW", "Audi", "Porsche", <45 elementos vacíos>, "Renault"]

// Cómo preguntar si es un Array o arreglo
console.log(Array.isArray(autos)); // true

console.log(autos instanceof Array); // true, preguntamos si la variable es una instancia de la clase Array
