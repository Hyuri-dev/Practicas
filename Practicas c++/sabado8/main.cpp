#include <iostream>
#include <cstdlib>
/* hacer programa que ingrese el nombre del trabajador, el sueldo del trabajador, calcular entonces el bono de alimentacion en un 80%, bono de asistencia 70% y que muestre el total a cobrar del
trabajador*/
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	system("color 34");
	
	int sueldo, bono_alimentacion, bono_asistencia ,total_sueldo;
	string trabajador;
	
	cout <<"Ingrese el nombre del trabajador: ";cin>>trabajador;
	cout <<"Ingrese el sueldo del trabajador: "; cin>> sueldo;
	
	bono_alimentacion = sueldo * 0.80;
	
	cout<<"Bono de alimentacion: "<< bono_alimentacion<<endl;
	
	bono_asistencia = sueldo* 0.70;
	
	cout <<"Bono de asisencia: " << bono_asistencia << endl;
	
	total_sueldo = sueldo + bono_alimentacion + bono_asistencia;
	
	cout <<" Sueldo a cobrar del trabajador: " << total_sueldo << endl;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}