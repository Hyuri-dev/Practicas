import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from modulo_clientes import Clientes

class Master_panel: 
    def  __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Panel")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight() #Obtenemos el ancho y alto de la pantalla
        self.ventana.geometry("%dx%d+0+0" % (w, h)) #Definimos el tamaño de la ventana
        self.ventana.resizable(0,0)
        self.ventana.configure(bg="#D0E6FF")
        
        #Menu del panel principal
        self.menus = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menus)
        
        self.menu_salir = tk.Menu(self.menus, tearoff=0)
        self.menus.add_cascade(label="Salir", menu=self.menu_salir)
        
        #Columna donde estaran los botones de las opciones
        self.frame_column = tk.Frame(self.ventana, bg="white" )
        self.frame_column.place(x=0,y=0, width= 250, height= h)
        
        
        logo = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\logotiporb.png")
        logo = logo.resize((180,80))
        logo_tk = ImageTk.PhotoImage(logo)
        
        self.label_logo= tk.Label(self.frame_column, bg="White", image=logo_tk)
        self.label_logo.place(x=22, y=30, width=200, height=100)
        
        self.frame_buttons = tk.Frame(self.frame_column, bg="blue")
        self.frame_buttons.place(x=0, y=220, width=250, height=750)
        
        imagen = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\mcliente.png")
        imagen = imagen.resize((100 , 100))
        imagen_tk = ImageTk.PhotoImage(imagen)
        
        self.clientes = tk.Button(self.frame_buttons, image=imagen_tk, text="Clientes", font=("Arial", 18, "bold") , command=Clientes)
        self.clientes.place(x=0, y=0, width=250, height=250)
        self.clientes.config(bg="white", compound="bottom", relief="groove", border=0.5)
        
        imagen2 = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\caja.png")
        imagen2 = imagen2.resize((100 , 100))
        imagen_tk2 = ImageTk.PhotoImage(imagen2)
        
        self.pedidos = tk.Button(self.frame_buttons, image=imagen_tk2, text="Pedidos", font=("Arial", 18, "bold"))
        self.pedidos.place(x=0, y=250, width=250, height=250)
        self.pedidos.config(bg="white", compound="bottom", relief="groove", border=0.5)
        
        imagen3 = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\camion.png")
        imagen3 = imagen3.resize((100 , 100))
        imagen_tk3 = ImageTk.PhotoImage(imagen3)
        
        self.carga = tk.Button(self.frame_buttons, image=imagen_tk3, text="Carga y Despachos", font=("Arial", 18, "bold"))
        self.carga.place(x=0, y=500, width=250, height=250)
        self.carga.config(bg="white", compound="bottom", relief="groove", border=0.5)
        
        icon_help = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\soporte-tecnico.png")
        icon_help = icon_help.resize((30 , 30))
        icon_help_tk = ImageTk.PhotoImage(icon_help)
        
        # Boton de aiuda e info del creador
        self.butonhelp = tk.Button(self.frame_column, image=icon_help_tk, text="Ayuda", font=("Arial", 12,))
        self.butonhelp.place(x=0, y=965 , width=250, height=50)
        self.butonhelp.config(bg="white",compound="bottom", relief="flat")
        
        
        #logo de la esquna inferior derecha
        logo2 = Image.open("F:\\Programacion\\Proyectos\\Sistema\\assets\\logov.png")
        logo2 = logo2.resize((300,300))
        logo2_tk = ImageTk.PhotoImage(logo2)
        
        self.label_logo2= tk.Label(self.ventana, bg="#D0E6FF", image=logo2_tk)
        self.label_logo2.place(x= 1615, y=730)
        
        
        
        
        self.ventana.mainloop()

# Master_panel()
