import tkinter as tk
from PIL import Image , ImageTk
from tkinter import filedialog , messagebox

class Myapp:
    def __init__(self):
        self.main = tk.Tk()
        self.main.geometry("400x300")
        self.main.iconbitmap("C:\\Users\\Jefferson\\Documents\\Desarrollo\\Python\\POO\\POO\\tkinter\\assets\\images\\folders_icons.ico")
        
        self.button_change = tk.Button(self.main, text="Cambiar icono", command= self.cambiar_icono)
        self.button_change.pack()
        self.main.mainloop()
    
    def cambiar_icono(self):
        ruta = filedialog.askopenfilename(title="Seleccione un archivo .ico" , filetypes=(("Archivos ico", ".ico"),("Todos los archivos", "*.*")))
        if ruta:
            try:
                self.main.iconbitmap(ruta)
            except Exception as e:
                print(f"Error al cambiar el icono {e}")

main = Myapp()