#include <iostream>

using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	
		system("color 34");
	
	int sueldo, bono_patria, total, produccion, sueldo_intermedio;
	string trabajador;
	
	cout <<"Ingrese el nombre del trabajador: ";cin>>trabajador;
	cout <<"Ingrese el sueldo del trabajador: "; cin>> sueldo;
	
	sueldo_intermedio = 1500;
	
	if (sueldo >= 1000) {
		
		bono_patria = sueldo * 0.70;
		
		cout << "Bono patria es: "<< bono_patria << endl;
		
		total = sueldo + bono_patria;
		
		cout << "El sueldo a cobrar es de: " << total << endl;
		
	} else if (sueldo >2000) {
	
		produccion = sueldo * 0.50;
	
		cout <<"La produccion en base al salario es: " << produccion << endl;
	
		total = sueldo + produccion;
		
		cout <<"El sueldo a cobrar es de: " << total << endl;
		
	} else {
			
			total = sueldo_intermedio;
			cout << "El sueldo a obrar es: " << total << endl;
		}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
return 0;	
}