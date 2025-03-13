#include <iostream>

using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	/* declaramos las variables a utilizar */
	int nota1 , nota2, nota3, nota4 ,nota5, total, promedio;
	
	cout <<"Ingrese la primera nota: "; cin >> nota1;
	cout <<"Ingrese la segunda nota: "; cin >> nota2;
	cout <<"Ingrese la tercera nota: "; cin >> nota3;
	cout <<"Ingrese la cuarta nota: "; cin >> nota4;
	cout <<"Ingrese la quinta nota: "; cin >> nota5;
	
	total = nota1 + nota2 + nota3 + nota4 + nota5;
	promedio = total / 5;
	
	cout <<"El promedio del alumno es: " <<promedio;
	
	
	
	
	
	
	return 0;
}