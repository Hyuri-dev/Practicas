import tkinter as tk
# from tkcalendar import *


class Clientes:
    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("Clientes")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        
        self.barra_herramientas = tk.Frame(self.ventana, width = 800 , height= 40, bg="#0067C8")
        self.barra_herramientas.place(x=0 , y=0)
        
        
        self.frame1 = tk.Frame(self.ventana, width=500, height=600, bg="blue")
        self.frame1.place(x= 0 , y= 40)
        
        
        
        
        self.ventana.mainloop()
        

Clientes()