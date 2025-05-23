
#Creamos una clase persona que tiene un atributo nombre y dos metodos (funciones) inicializar e imprimir


class Persona:
  
  def inicializar (self, nom): # constructor de la clase que espera un argumento nom (nombre)
    self.nombre = nom
        
  def imprimir (self): # Metodo que imprime el nombre de persona
    print("Nombre: " , self.nombre)

# Principal 

Persona1 = Persona() # Creamos un objeto de la clase persona, llamando a la clase Persona

# Inicializamos el objeto Persona1 con el nombre que espera recibir

Persona1.inicializar("Mandarino") 

Persona1.imprimir() # Imprimimos por consola el nombre, hemos llamado el metodo imprimir de la clase Persona

#Cremos otra instancia de la clase persona

Persona2 = Persona()

Persona2.inicializar("Bayley")

Persona2.imprimir()

