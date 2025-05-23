# Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto (concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)

class Plano:
  def __init__(self, x , y):
    self.x = x
    self.y = y
    
  def imprimir (self):
    print("Coordenada del punto")
    print("(",self.x,",",self.y,")")
    
  def imprimir_cuadrante (self):
    if self.x > 0 and self.y > 0 :
      print("Primer cuadrante: ")
    elif self.x < 0 and self.y > 0:
      print("Segundo Cuadrante")
    elif self.x > 0 and self.y < 0 :
      print("Cuarto Cuadrante")
    elif self.x < 0 and self.y < 0 :
      print("Tercer Cuadrante")
    else:
      print("Ha ingresado valores invalidados, por favor ingrese un valor que sea valido")


coordenadas = Plano(-3 , 5)
coordenadas.imprimir()
coordenadas.imprimir_cuadrante ()