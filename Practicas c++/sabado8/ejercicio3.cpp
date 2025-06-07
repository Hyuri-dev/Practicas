#include <iostream>
#include <cstdlib>

using namespace std;

// declaramos una funcion

/* para crear funciones en c++ necesitamos usar void, la estructura de una funcion es de la siguiente manera 

void nombre_funcion (tipo de dato que retorna la funcion) {

codigo de lafuncion

}
*/

void operaciones (int nro1, int nro2){

    cout <<"Ingrese el primer valor: "; cin >> nro1; /*cin almacena variables y cout es para mostrar un mensaje en pantalla*/
    cout <<"Ingrese el segundo valor: "; cin >> nro2; /*cin almacena variables y cout es para mostrar un mensaje en pantalla*/

    int suma, resta, multiplicacion, division;

    suma = nro1 + nro2;
    resta = nro1 - nro2;
    multiplicacion = nro1 * nro2;
    division = nro1 / nro2;
    
    cout <<"La suma es: " <<suma<< endl;/*endl permite crear saltos de linea para organizar mejor el codigo*/
    cout <<"La resta es: " << resta << endl;/*endl permite crear saltos de linea para organizar mejor el codigo*/
    cout <<"La multiplicacion es: " << multiplicacion << endl;/*endl permite crear saltos de linea para organizar mejor el codigo*/
    cout <<"La division es: " << division << endl;/*endl permite crear saltos de linea para organizar mejor el codigo*/
}

int main (int argc, char** argv){

    char respuesta; /* declaramos una variable tipo char, variables char son  Para valores tipo carácter. Un carácter es un símbolo, como los que usamos para escribir, 
    por ejemplo ‘T’, ‘c’, ‘r’, ‘/’, ‘5’. En este último caso el 5 será considerado*/
    bool continuar = true; /* Declaramos una variable bool, las variables tipo bool son para almacenar valores verdaderos o falsos (true or false)*/
    int nro1 , nro2;


    while (continuar){ /* while se utiliza para crear una condicion, en este caso lo utilizamos para que mientras continuar sea verdadero el programa pueda permanecer activo
        asi tener mejor control sobre el, al finalizar la operacion nos preguntara si queremos continuar o no, si le damos que si, nos retornara nuevammente al inicio de nuestro
        script pero si se responde se cerrara el script*/

        operaciones(nro1, nro2); /*llamamos a la funcion que se creo y con los parametros que se van a utilizar*/

        cout <<"Desea continuar? (Y/N):"; cin >> respuesta;

        /* Creamos un if para poder crear el abanico de opciones para el usuario, si quiere volver a hacer una operacion o no*/
        if (respuesta == 'N'  || respuesta == 'n'){
            continuar = false; //declaramos false el continue para que el while se cierre y termine el programa
        } else if (respuesta == 'Y'  || respuesta == 'y'){
            continuar = true; //declaramos true para que el while se mantenga y el programa siga ejecutandose
        } else { /*en el else, que seria la opcion por hacer por si se ingresa una respuesta invalida aqui se procedera a cerrar el programa, 
            llamamos a la variable coninuar y la definimos como false para que el while se pase a false y se cierre el programa*/
            cout <<"Opcion incorrecta, se procedera a cerrar el programa";
            continuar = false;
        }
    }
    // declaramos las variables a utilizar en nuestro script
    return 0;
}