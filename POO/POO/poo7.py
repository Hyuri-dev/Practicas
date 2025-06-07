#Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa.

from ast import While
from pickletools import OpcodeInfo


class Gestion_alumnos:
    def __init__(self):
        self.alumnos = []
        self.notas = []
    
    def menu (self):
        opcion = 0        
        while opcion != 5: 
            print("--------- menu de gestion de alumnos ---------, \n 1.Cargar alumnos \n 2.Listado de alumnos \n 3.Mostrar alumnos con notas (aprobados) \n 4. Mostras alumnos con notas (reprobados) \n 5.Salir del script")
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                self.cargar_alumnos()
            elif opcion == 2:
                self.listado_alumnos()
            elif opcion == 3:
                self.alumnos_aprobados()
            elif opcion == 4:
                self.alumnos_reprobados()
            
    
    def cargar_alumnos (self):
        
        try:
            for x in range(5):
                self.alumnos.append(input("Ingrese el nombre de un alumno: "))
                self.notas.append(int(input("Ingrese la nota del estudiante: ")))
                print(f"Listado de alumnos ingresados: {self.alumnos[x]},  nota: {self.notas[x]}")
        except:
            print("Alumno no se pudo ingresar al listado, por favor intente de nuevo o revise el error")
            return
    
    def listado_alumnos (self):
        print("------------- listado de alumnos -------------")
        for x in range (5):
            print(self.alumnos[x] , self.notas[x]) #iteramos en orden y en conjunto la lista
            
        print("________________________________________")
        
    def alumnos_aprobados (self):
        print("------- Alumnos aprobados -------")
        for x in range (5):
            if self.notas [x] >= 10:
                print(self.alumnos[x], self.notas[x])
                
    def alumnos_reprobados (self):
        print("------- Alumnos reprobados -------")
        for x in range (5):
            if self.notas [x] <= 9:
                print(self.alumnos[x], self.notas[x])


alumno1 = Gestion_alumnos()
alumno1.menu()
