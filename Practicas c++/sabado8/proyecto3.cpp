#include <iostream>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	/* Declaramos las variables a utilizar*/
	int precio , cantidad, total,total2,totalgeneral, descuento, iva; 
	string producto;
	
	cout <<"Ingrese el nombre del producto: "; cin >> producto;
	cout <<"Ingrese la cantidad del producto: "; cin >> cantidad;
	cout <<"Ingrse el precio del producto: "; cin >> precio;
	cout <<"------------------------------------------------------ ";
	
	total = precio * cantidad;
	
	descuento = total * 0.05;
	
	total2 = total - descuento;	
	
	iva = total2*0.16;
	
	totalgeneral = total2 + iva;
	
	
	cout<<"El producto es: "<< producto<< endl;
	cout<<"El precio del producto es: " << precio << endl;
	cout<<"Total de la compra es: " << total << endl;
	cout<<"Total con descuento: " << total2 << endl;
	cout<<"iva: " << iva << endl;
	
	cout<<"El total con iva y descuento es: "<< totalgeneral;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}