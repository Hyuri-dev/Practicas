import tkinter as tk 
from tkinter import filedialog


class MyApp: 
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("Lector de archivos")
        self.main.geometry("400x300")
        
        self.title = tk.Label(self.main, text="Ingrese un archivo para leer")
        self.title.pack()
        
        self.text = tk.Text(self.main, wrap="word", width= 40 , height= 10) #text es un widget de tkinter que muestra texto, wrap es un metodo que tiene para acomodar el texto en base a 3 opciones
        self.text.pack(pady= 20)
        
        self.buton_abrir = tk.Button(self.main, text="Abrir archivo", command= self.abrir_archivo)
        self.buton_abrir.pack(pady= 5)
        
        self.buton_cancelar = tk.Button(self.main, text="Cancelar", command= self.limpiar)
        self.buton_cancelar.pack(pady= 5)
        self.main.mainloop()
        
    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(title="Selecciona un archivo de texto" , filetypes=(("Archivos de texto", ".txt"), ("Todos los archivos", "*.*")))
        
        if ruta:
            try:
                with open (ruta , "r") as archivo:
                    contenido = archivo.read()
                    self.text.delete('1.0', tk.END)
                    self.text.insert(tk.END, contenido)
                    self.title.configure(text="")
            except Exception as e:
                self.text.delete('1.0', tk.END)
                self.text(tk.END, f"Error al leer el archivo {e}")
                
    def limpiar (self):
        try:
            self.text.delete("1.0", tk.END)
            self.title.configure(text="Ingrese un archivo para leer")
        except Exception as e:
            print(f"Error al reiniciar el programa {e} ")

main = MyApp()