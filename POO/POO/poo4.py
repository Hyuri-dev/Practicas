# Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su perímetro y su superficie.

class Cuadrado :
  def __init__(self):
    self.lado = int(input("Ingrese cuanto mide el lado del cuadrado: "))
    self.area = self.lado
    
  def imprimir_info_cuadrado (self):
    print(f"El cuadrado tiene un lado de: {self.lado} cm")
    print(f"El cuadrado tiene una superficie de: {self.area}")
    
  def calcular_perimetro (self):
    perimetro = self.lado * 4
    print(f"El perimetro del cuadrado es de: {perimetro} cm")
  
  def calcular_superficie (self):
    superficie = self.area * self.area
    print (f"La superficie del cuadrado es: {superficie}cm")


cuadrado1 = Cuadrado()
cuadrado1.imprimir_info_cuadrado()
cuadrado1.calcular_perimetro()
cuadrado1.calcular_superficie()