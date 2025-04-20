#Importamos librerias 
import tkinter as tk
import sqlite3
from tkinter import messagebox as mb
from tkinter import ttk
from master_panel import Master_panel
from tkinter import PhotoImage
from PIL import Image, ImageTk


#Variables, funciones y clases

#Clase usuario, establece conexion y consulta los datos
class Usuario: 
    def abrir(self):
        conn = sqlite3.connect("F:\\Programacion\\Proyectos\\Sistema\\usuarios.db")
        return conn
    print("Conexion establecia correctamente")
    
    def consultar(self,datos):
        resultado = False
        try:
            with self.abrir() as cone:
                cursor = cone.cursor()
                cursor = cone.execute("select * from usuario where usuario=? and contraseña=?", (datos[0], datos[1]))
                resultado = cursor.fetchone()
                print("Resultado: ", resultado)
        finally:
            cursor.close()
        return resultado

#Clase login aqui se hace la verificacion de credenciales del usuario a entrar en el sistema. 
class Login: 
    def __init__(self):
        self.obj_usuario = Usuario () #llamamos a la clase usuario a nuestro login
        
        #Ventana del login
        self.window = tk.Tk()
        self.window.title("Login / inicio de sesion")
        self.window.geometry("800x600") 
        self.window.resizable(False, False)
        self.window.iconbitmap("F:\\Programacion\\Proyectos\Sistema\\assets\\icon_login4.ico")
        
        self.frame_logo = tk.Frame(self.window, width=400, height=600, bg="White")
        self.frame_logo.place(x=0, y=0)
        
        image = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\logotiporb.png")
        image = image.resize((360,78))
        self.login_logo= ImageTk.PhotoImage(image)
        
        self.label_logo = tk.Label(self.frame_logo, image=self.login_logo)
        self.label_logo.place(y=200, x=15)
        self.label_logo.config(bg="White")
        
        self.frame_login = tk.Frame(self.window, width=400, height=600, bg="#0B6DB6")
        self.frame_login.place(x=400,y=0)
        
        #Etiquetas y cajas de texto
        self.lbl_twelcome = tk.Label(self.frame_login, text="Bienvenido", fg="#CC0606", bg="#0B6DB6")
        self.lbl_twelcome.place(anchor= "center", relx=0.3 , rely=0.1)
        self.lbl_twelcome.config(font=("Helvetica", 28, "bold"))
        
        self.lbl_title = tk.Label(self.frame_login,text="Distribuidora America Del Centro", fg="White", bg="#0B6DB6")
        self.lbl_title.place(anchor="center", relx= 0.5, rely=0.2)
        self.lbl_title.config(font=("Helvetica",18, "bold"))
        
        self.frame_forms = tk.Frame(self.frame_login, width=500, height=300, bg="#0B6DB6")
        self.frame_forms.place(anchor="center", relx=0.5, rely=0.5)
        
        self.lbl_usuario = tk.Label(self.frame_forms, text="Usuario:", fg="White")
        self.lbl_usuario.place(anchor="center", relx=0.29, rely=0.1)
        self.lbl_usuario.config(font=("Helvetica", 18), bg="#0B6DB6")
        
        self.txb_usuario =tk.Entry(self.frame_forms)
        self.txb_usuario.place(anchor="center", relx=0.5, rely=0.20, width=300, height= 35)
        
        self.lbl_contraseña = tk.Label(self.frame_forms, text="Contraseña:", fg="White", bg="#0B6DB6")
        self.lbl_contraseña.place(anchor="center", relx=0.32, rely=0.4)
        self.lbl_contraseña.config(font=("Helvetica",18))
        
        self.txb_contraseña = tk.Entry(self.frame_forms, show="*")
        self.txb_contraseña.place(anchor="center", relx=0.5, rely=0.5, width=300, height=35)
        
        #Botones
        
        self.frame_buttons = tk.Frame(self.frame_forms, width=300, height=50, bg="#0B6DB6")
        self.frame_buttons.place(anchor="center", relx=0.5, rely=0.7)
        
        self.btn_login = ttk.Button(self.frame_buttons, text="Entrar", command= self.verificar)
        self.btn_login.place(anchor="center", relx=0.3, rely=0.5)
        
        self.btn_cancel= ttk.Button(self.frame_buttons, text="Salir")
        self.btn_cancel.place(anchor="center", relx=0.7, rely=0.5)
        
        self.window.mainloop()
        
        #Funcion de verificacion de usuario
    def verificar (self):
        if self.txb_usuario.get() == "" or self.txb_contraseña.get() =="":
            mb.showerror("Error login", "Debe rellenar los campos")
            return
        datos = (self.txb_usuario.get(), self.txb_contraseña.get())
        if self.obj_usuario.consultar(datos) != None:
            mb.showinfo("login","Bienvenido al sistema de logistica y ventas diacenca")
            self.window.destroy()
            Master_panel()

