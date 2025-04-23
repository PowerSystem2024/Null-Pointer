class DispositivoEntrada{
    constructor(tipoEntrada,marca,){
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }
    get tipoEntrada(){
        return this._tipoEntrada;
    }
    set tipoEntrada(tipoEntrada){
        this._tipoEntrada = tipoEntrada;
    }
    get marca(){
        return this._marca;
    }
    set marca(marca){
        this._marca = marca;
    }
   
    
}
class Raton extends DispositivoEntrada{
    static contadorRatones = 0;

    constructor(tipoEntrada,marca){
        super(tipoEntrada,marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    get idRaton(){
        return this._idRaton;
    }
    toString(){
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

let raton1 = new Raton("USB","HP");
console.log(raton1.toString());
let raton2 = new Raton ("Bluetooth","Dell");
console.log(raton2.toString());

class Teclado extends DispositivoEntrada{
    static contadorTeclado = 0;

    constructor(tipoEntrada,marca){
        super(tipoEntrada,marca)
            this._idTeclado = ++Teclado.contadorTeclado;
    }
    get idTeclado(){
        return this._idTeclado;
    }
    toString(){

    return`Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
    }   
}
let teclado1 = new Teclado("USB", "HP");
console.log(teclado1.toString());
let teclado2 = new Teclado("Bluetooth", "Acer");
console.log(teclado2.toString());

class Monitor{
    static contadorMonitores = 0;
    constructor (marca, tamanio){
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._tamanio = tamanio;
    }
    get idMonitor(){
        return this._idMonitor;
    }
    toString(){
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamanio}]`
    }
}
let monitor1 = new Monitor("HP", 15);
let monitor2 = new Monitor("Dell", 27);
console.log(monitor1.toString());
console.log(monitor2.toString());


class Computadora {
    static contadorComputadoras = 0;
    constructor (nombre, monitor, raton, teclado){
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._teclado = teclado;
        this._raton = raton;
    }
    toString(){
        return `Computadora ${this._idComputadora}: ${this._nombre}\n ${this._monitor}\n ${this._teclado}\n ${this._raton}\n`
    }
}

let computadora1 = new Computadora("HP", monitor1, raton1, teclado1)
console.log(computadora1.toString());
console.log(`${computadora1}`); //LLAMA AUTOMATICAMENTE AL TOSTRING
let computadora2 = new Computadora("Acer" , monitor2,raton2,teclado2)
console.log(`${computadora2}`);

class Orden{
    static contadorOrdenes = 0;

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = []; //ARREGLO VACIO
    }
    get idOrden(){
        return this._idOrden;
    }
    agregarComputadora(computadora){
        this._computadoras.push(computadora); //AGREGAMOS LOS OBJETOS
    }
    mostrarOrden(){ //EQUIVALE AL TOSTRING
        let computadorasOrden = ''; //variable temporal
        for(let computadora of this._computadoras){
            computadorasOrden += '\n${computadora}';
        }
        console.log(`Orden: ${this.idOrden}, Computadoras: ${computadorasOrden}`);
    }
}

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.agregarComputadora(computadora2);//SE PUEDE REPETIR UNA ORDEN
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.agregarComputadora(computadora1);
orden2.mostrarOrden();