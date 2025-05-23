# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

# Definir dos objetos de la clase Alumno.

class Alumno:
  def inicializar (self, nombre, nota):
    self.nombre = nombre
    self.calificacion = nota
    
  def imprimir (self):
        print(f"Nombre: {self.nombre} , Calificacion: {self.calificacion}")
        
  def estado (self):
    if self.calificacion >= 4:
        print(f"Nombre: {self.nombre} ha aprobado la materia con una Calificacion de: {self.calificacion}")
    else:
        print(f"El alumno {self.nombre} no saco el minimo para poder pasar la materia, calificacion: {self.calificacion}")



Alumno1 = Alumno()
Alumno1.inicializar(input("Ingrese el nombre del Alumno: "), int(input("Ingrese la calificacion del alumno: ")))
Alumno1.imprimir()
Alumno1.estado()

Alumno2 = Alumno()
Alumno2.inicializar("Maria" , 5)
Alumno2.imprimir()
Alumno2.estado()