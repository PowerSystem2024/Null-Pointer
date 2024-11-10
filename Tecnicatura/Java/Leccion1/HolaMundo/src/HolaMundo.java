
import java.util.Scanner;



public class HolaMundo {

    public static void main(String[] args) {

        /*System.out.println("Hola mundo desde Java");

        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //TIPO STRING
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);

        //Var - inferencia de tipos en JAVA
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab
        //PARA EJECUTAR SHIFT + F6
        //Reglas para definir una variable en JAVA

        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio : Caracteres Especiales con JAVA
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n"+nombre); 
        System.out.println("Tabulador: \t" + nombre);// tabulador un espacio para centrar
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroseso:\b\b"+nombre);  // Caracter de rRetroseso                
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas Dobles:\""+nombre+"\"");
          

        // Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado:  "+ titulo2+" "+usuario2);*/
 /*byte numEnteroByte = (byte)127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long:" + Long.MIN_VALUE);
        System.out.println("Valor maximo del long:" + Long.MAX_VALUE);*/
 /* float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float: " + Float.MIN_VALUE);
        System.out.println("El valor maximo de float: " + Float.MAX_VALUE);
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de double:"+Double.MIN_VALUE);
        System.out.println("El valor maximo de double:"+Double.MAX_VALUE);*/
        // INFERENCIA DE TIPOS VAR Y TIPOS PRIMITIVOS
        /*var numEntero = 20; // Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; 
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        //Tipos primitivos CHAR
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; // indicamos a JAVA la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        
        char varCaracterDecimal = 36;//VALOR DECIMAL DEL JUEGO DE CARACTERES UNICODE
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracteresSimbolo = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracteresSimbolo = " + varCaracteresSimbolo);
        
        var varCaracter1 = '\u0024'; // indicamos a JAVA la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter);
        var varCaracterDecimal1 = (char)36;//VALOR Entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal);
        var varCaracteresSimbolo1 = '$'; // Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracteresSimbolo1 = " + varCaracteresSimbolo);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        //TIPOS PRIMITIVOS TIPO BOOLEANOS
        /* var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){    
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");  
        }
      // ALGORITMO: ¿Es mayor de edad?
      var edad = 15; 
      //var adulto = edad >= 18;
      if (edad >= 18){
          System.out.println("Eres mayor de edad");
      }
      else{
          System.out.println("Eres menor de edad");
      }*/
        //Conversion de tipos primitivos
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //PEDIR UN VALOR
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad:");
        edad = Integer.parseInt (entrada.nextLine());
        System.out.println("edad = " + edad);
       
       //Conversion de tipos primitivos Parte 2
       var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(5);
        System.out.println("fraseChar = " + fraseChar);*/
        
       /* int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println(" solucion de la suma = " +  solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2; // Solo detecta que es double
        System.out.println("solucion2 resultado de la division = " + solucion2);
        
        solucion = num1 % num2;// GUARDA EL RESIDUIO ENTERO DE LA DIVISION
        System.out.println("solucion  = " + solucion); // 5 /4
        
        if (num1 % 2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero impar");*/
       
       int varNum1 = 1, varNum2 = 4;
       int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = "+ varNum3);
        
        varNum1 += 1; // varNum1 = varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 5;
        System.out.println("varNum2 = " + varNum2);
        
        varNum3 *= 2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 /= 3;
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 %= 4;
        System.out.println("varNum2 = " + varNum2);
        
        
       
    }
}
