# Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa.

class Agenda:
    def __init__(self):
        self.name = []
        self.phone = []
        self.mail = []
        self.adress = []
    
    def menu (self):
        opcion = 0
        while opcion != 5:
            print("---------------- Agenda---------------- \n 1. Cargar un contacto \n 2. Listado completo de la agenda \n 3. Consulta de contacto \n 4. Editar contacto \n 5. Salir del sistema")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.consultar()
            elif opcion == 4:
                self.editar()
            elif opcion == 5:
                print("Saliendo del sistema... ")

                
            
    
    def cargar (self):
        
        self.rango = int(input("Ingrese cuantas personas va a añadir en la agenda: "))
        
        for x in range (self.rango):
            try:
                self.name.append (input("Ingrese el nombre de la persona: "))
                self.phone.append (input("Ingrese el telefono de la persona: "))
                self.mail.append (input("Ingrese el correo electronico de la persona: "))
                self.adress.append (input("Ingrese la direccion del contacto: "))
                print(f"Se registraron {len(self.name)} contactos exitosamente.")
            except:
                print("No se ha podido registrar el/los contactos en la agenda, intente nuevamente.")
                return
    
    def listar (self):
        print("---------------- Lista de contactos ----------------")
        for x in range (self.rango):
            print(self.name[x], self.phone[x], self.mail[x],self.adress[x])
            
    def consultar (self):
        print("---------------- Consultar contactos ----------------")
        buscador = input("Ingrese el nombre del contacto: ")
        
        if buscador in self.name:
            self.name.index(buscador)
            print(f"{self.name} \n {self.phone} \n {self.mail} \n {self.adress}")
            print(f"el contacto {buscador} existe en la agenda")
        else:
            print("No encontrado")

    def editar (self):
        print("---------------- Editar contacto ----------------")
        buscador = input("Ingrese el nombre del contacto a cambiar: ")
        
        if buscador in self.name:
            indice = self.name.index(buscador)
            print("\nDatos actuales del contacto:")
            print(f"Nombre: {self.name[indice]}")
            print(f"Teléfono: {self.phone[indice]}")
            print(f"Correo: {self.mail[indice]}")
            print(f"Dirección: {self.adress[indice]}")
            
            print("\nIngrese los nuevos datos:")
            self.name[indice] = input("Nuevo nombre (dejar vacío para mantener el actual): ") or self.name[indice]
            self.phone[indice] = input("Nuevo teléfono (dejar vacío para mantener el actual): ") or self.phone[indice]
            self.mail[indice] = input("Nuevo correo (dejar vacío para mantener el actual): ") or self.mail[indice]
            self.adress[indice] = input("Nueva dirección (dejar vacío para mantener el actual): ") or self.adress[indice]
            
            print("\nContacto actualizado exitosamente!")
            print("Datos actualizados:")
            print(f"Nombre: {self.name[indice]}")
            print(f"Teléfono: {self.phone[indice]}")
            print(f"Correo: {self.mail[indice]}")
            print(f"Dirección: {self.adress[indice]}")
        else:
            print("\nContacto no encontrado en la agenda")






contactos = Agenda()
contactos.menu()
