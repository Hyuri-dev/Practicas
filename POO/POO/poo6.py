# Llamada de metodos desde otros metodos de la misma clase

#Es posible llamar a un metodo desde otro metodo siempre y cuando la llamada se haga desde una instancia de la clase creada

class Operaciones : 
    def __init__(self):
        self.valor1 = float(input("Ingrese el primer valor: "))
        self.valor2 = float(input("Ingrese el segundo valor: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    
    def mostrar_valores (self):
      print(f"Primer valor: {self.valor1} ")
      print(f"Segundo valor: {self.valor2}")
    
    def suma (self):
      resultado = self.valor1 + self.valor2
      print(f"El resultado de la suma es: {resultado}")
      
    def resta (self):
      resultado = self.valor1 - self.valor2
      print(f"El resultado de la resta es: {resultado}")
      
    def multiplicacion (self):
      resultado = self.valor1 * self.valor2
      print(f"El resultado de la multiplicacion es: {resultado}")
      
    def division (self):
      resultado = self.valor1 / self.valor2
      print(f"El resultado de la division es: {resultado}")

operacion = Operaciones()
