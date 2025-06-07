#include <iostream>
#include <cstdlib>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	int carnet , uniforme , notas_certificadas, constancia_estudio , wifi, total_pagar, cuatrimestre;
	string estudiante;
	
	cout << "Ingrese el nombre del estudiante "; cin >> estudiante;
	cout <<"Ingrese el costo del cuatrimestre: " ; cin >> cuatrimestre;
	
	carnet = cuatrimestre * 0.20;
	
	cout <<"costo del carnet: " << carnet << endl;
	
	uniforme = cuatrimestre * 0.30;
	
	cout <<"Costo del uniforme: " << uniforme << endl;
	
	notas_certificadas = cuatrimestre * 0.40;
	
	cout <<"Notas certificadas: " << notas_certificadas << endl;
	
	constancia_estudio = cuatrimestre * 0.60;
	
	cout <<"Constancia de estudio: " << constancia_estudio << endl;
	
	wifi = cuatrimestre * 0.90;
	
	cout <<"Wifi: " << wifi << endl;
	
	total_pagar = cuatrimestre + carnet + uniforme + notas_certificadas + constancia_estudio + wifi;
	
	cout <<"Total a pagar del cuatrimestre: " << total_pagar << endl;
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	return 0;
}