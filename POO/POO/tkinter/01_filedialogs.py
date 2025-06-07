import tkinter as tk
from tkinter import filedialog
from PIL import Image , ImageTk

class MyApp:
    def __init__(self):
        
        #Inicializacion de la app con sus atributos
        self.main = tk.Tk()
        self.main.geometry("400x300")
        self.main.title("filedialogs")
        
        #mensaje con label
        self.image = tk.Label(self.main, text="Ingrese una imagen para mostrar...")
        self.image.pack(pady= 30)
        
        #Boton para buscar una imagen
        self.button = tk.Button(self.main, text="Buscar imagen", command= self.buscar_abrir)
        self.button.pack()
        
        self.main.mainloop()
    
    #funcionalidad , metodos
    def buscar_abrir (self):
        #Filedialog nos permite tener metodos para poder guardar o ubicar archivos, en este caso utilizamos askopenfilename para abrir un archivo y que nos devuelva la ruta donde esta.
        self.ruta_imagen = filedialog.askopenfilename()
        
        # Utilizamos un if para comprobar si tomó la imagen o no y asi decidir que hacer en este caso lo convertimos en una imagen para tkinter con PIL e imageTK
        if self.ruta_imagen:
            self.imagen = Image.open(self.ruta_imagen)
            self.imagen=ImageTk.PhotoImage(self.imagen)
            self.image.config(image= self.imagen, text="") # Utilizamos el metodo config para poder meter la imagen en el label y asi poder mostrarla, volvemos a llamar al texto para dejarlo vacio para que solo se muestre la imagen
            print(f"Archivo cargado con exito, ruta: {self.ruta_imagen}")
            # self.image.config(image= imagen)
        else:
            print(f"Error, no ha sido posible cargar el archivo intente nuevamente.")


example = MyApp()
