
package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[]args){
        var conteo = 0;//INFERENCIA DE TIPOS
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++; // Vamos aumentando en uno la variable
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        //USO DE LAS PALABRAS BREAK Y CONTINUE JUNTO A LAS ETIQUETAS (LABELS)
        inicio:
        for(var contado = 0 ;contado < 7 ; contado++){
            if(contado % 2 == 0){
                System.out.println("contado = " + contado);
                break inicio;
            }    
        }
        
        for(var contado = 0 ;contado < 7 ; contado++){
            if(contado % 2 != 0){
                continue; //VAMOS A LA SIGUIENTE ITERACION               
            }    
            System.out.println("contado = " + contado);
        }
    }
}
