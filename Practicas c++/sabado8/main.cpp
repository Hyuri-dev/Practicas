#include <iostream>
#include <cstdlib>
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	/*Declaramos un color*/
	system ("color 1a");
	
	/* declaramos todas las variables a utilizar en nuestro script*/
	int nro1 , nro2, suma,resta,multiplicacion,division;
	
	cout <<"Ingrese el primer valor: "; cin >> nro1;  /*cin almacena variables y cout es para mostrar un mensaje en pantalla*/
	cout <<"Ingrese el segundo valor: "; cin >> nro2; 
	
	suma = nro1 + nro2;
	resta = nro1 - nro2;
	multiplicacion = nro1 * nro2;
	division = nro1 / nro2;
	
	
	cout <<"La suma es: " << suma << endl; /*endl permite crear saltos de linea para organizar mejor el codigo*/
	cout <<"La resta es: " << resta<< endl;
	cout <<"La multiplicacion es: " << multiplicacion << endl;
	cout <<"La division es: " << division << endl;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}