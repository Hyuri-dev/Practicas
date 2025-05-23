# Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones : 
    def __init__(self):
        self.valor1 = float(input("Ingrese el primer valor: "))
        self.valor2 = float(input("Ingrese el segundo valor: "))
    
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
operacion.mostrar_valores()
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()
