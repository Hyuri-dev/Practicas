import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import write

#Funciones y logica del programa
selected_path = "" # creamos una variable global para la ruta donde queremos que se guarde nuestro archivo

def record (): # esta funcion se encarga de la accion de grabar, tiene definido un framerate (puede cambiarse ), una duracion que es establecida por el usuario, el nombre a escoger para el archivo y la demas logica
    framerate = 44100
    
    #los get primero se tienen que declarar pero luego convertirlos en los datos que necesitaremos mas adelante
    duration_str = entry_duration.get() 
    name_str = entry_namefile.get()
    try: # utilizamos un try para manejar mejor los casos que puedan presentarse. 
        duration = int(duration_str) # Aqui convertimos la duracion del principio en entero para poder crear la variable record_voice
        record_voice = sd.rec(int(duration * framerate), samplerate=framerate, channels= 1)
        sd.wait()
        name_file = str(name_str) # Aqui convertimos la variable name_str a string para poder adjuntarla como el nombre que se le coloca al archivo
        file = name_file + ".wav"
        
        # verificar seleccion de ruta
        if not selected_path: # Se revisa si esta seleccionado un directorio para guardar el archivo
            messagebox.showwarning("Error", "Seleccione una carpeta para guardar el archivo")
            return
        
        #crear ruta del archivo
        full_path = f"{selected_path}/{file}" # en este caso full path va a contener la ruta y al final el nombre del archivo para ser guardado
        write(full_path , framerate , record_voice)
        messagebox.showinfo("Grabacion terminada", "Grabacion creada con exito")
    except ValueError:
        messagebox.showwarning("Error", "Ingrese un valor numerico")
        

def save ():
    root_rename = tk.Tk()
    
    entry_duration = ttk.Entry(root_rename)
    entry_duration.pack()
    entry_duration.insert(0 , "inserte el nombre del archivo")
    
    save_button = ttk.Button(root_rename, text="Save in ...", command=select)
    save_button.pack()
    root_rename.mainloop()

def select (): #Declaramos una variable para seleccionar la ruta de guardado 
    
    #Traemos la variable global de la mismma manera (global) para que esta sea cambiada con la ruta que seleccionemos
    global selected_path
    selected_path = filedialog.askdirectory(initialdir="Descargas" , title="Guardar archivo")
    if selected_path: # verificamos que se haya seleccionado una ruta
        lbl_path = ttk.Label(root, text=f"Carpeta seleccionada: {selected_path}")
        lbl_path.grid(row= 7 , column= 0)
    else: 
        messagebox.showerror("Error", "Debe escoger una ruta")

#Interfaz

root = tk.Tk()
root.title("SoundRecorder")

label_title = tk.Label(root, text="VoiceRecorder", font=("Helvetica,", 25))
label_title.grid(row= 0, column= 0, pady= 25)

label_namefile = ttk.Label(root, text="Nombre de la grabacion:")
label_namefile.grid(row=1  , column=0, pady= 5)

entry_namefile = ttk.Entry(root)
entry_namefile.grid(row= 2 , column= 0)
entry_namefile.config(width=50)

label_duration = ttk.Label(root, text="Duracion de la grabacion")
label_duration.grid(row= 3 , column= 0, pady= 5)

entry_duration = ttk.Entry(root)
entry_duration.grid(row= 4 , column= 0, pady= 15)
entry_duration.config(width=50)

button_rec = ttk.Button(root, text="Record", command= record)
button_rec.grid(row= 5 , column= 0)

button_dir = ttk.Button(root, text="dir", command= save)
button_dir.grid(row= 6 , column= 0)


root.mainloop()