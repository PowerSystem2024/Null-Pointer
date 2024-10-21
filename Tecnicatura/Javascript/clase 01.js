// while
let contador = 0;
while (contador < 3) {
    console.log(contador);
    contador++;
}
console.log("fin del ciclo while");

// do while
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
} while (conteo < 3);
console.log("fin del ciclo de do while");

// for
for (let contando = 0; contando < 3; contando++) {
    console.log(contando);
}
console.log("fin del ciclo for");

// Palabra reservada break
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 == 0) {
        console.log(contando); // muestra el primer número par
        break; // rompe el ciclo después de encontrar el primer número par
    }
}
console.log("termina el ciclo al encontrar el primer número par");

// La palabra continue y etiquetas labels
inicio:
for (let contando = 0; contando <= 10; contando++) {
    if (contando % 2 !== 0) {
        continue inicio; // salta a la siguiente iteración cuando el número es impar
    }
    console.log(contando); // muestra solo los números pares
}
console.log("termina el ciclo"); 
