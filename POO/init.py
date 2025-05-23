#El metodo init

# # El método __init__ es un constructor que se ejecuta automáticamente al crear una instancia de la clase.
# Se utiliza para inicializar los atributos de la clase , es decir ya no se crea un metodo inicialiar

class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    def imprimir(self):
      print(f"Nombre: {self.nombre} sueldo: {self.sueldo}")
      
    def paga_impuestos (self):
      if self.sueldo >= 3000:
        print("Este empleado debe pagar impuestos")
      else:
        print("Este empleado no debe pagar impuestos aun")


Empleado1 = Empleado()
Empleado1.imprimir()
Empleado1.paga_impuestos()