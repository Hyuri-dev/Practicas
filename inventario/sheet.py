import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Notebook")
ventana.geometry("400x300")

# Crear el widget Notebook
panel_con_pestanas = ttk.Notebook(ventana)

# Crear los 'frames' que servirán como contenido de cada pestaña
pestana1 = ttk.Frame(panel_con_pestanas)
pestana2 = ttk.Frame(panel_con_pestanas)
pestana3 = ttk.Frame(panel_con_pestanas)

# Añadir las pestañas al Notebook
panel_con_pestanas.add(pestana1, text='Hoja 1')
panel_con_pestanas.add(pestana2, text='Hoja de Cálculos')
panel_con_pestanas.add(pestana3, text='Gráficos')

# Añadir widgets a la primera pestaña
etiqueta1 = ttk.Label(pestana1, text="Contenido de la primera pestaña.")
etiqueta1.pack(padx=10, pady=10)
boton1 = ttk.Button(pestana1, text="Botón 1")
boton1.pack(pady=5)

# Añadir widgets a la segunda pestaña
etiqueta2 = ttk.Label(pestana2, text="Aquí irían los datos de la hoja de cálculo.")
etiqueta2.pack(padx=10, pady=10)

# Añadir widgets a la tercera pestaña
etiqueta3 = ttk.Label(pestana3, text="Aquí se mostrarían los gráficos.")
etiqueta3.pack(padx=10, pady=10)

# Empaquetar el Notebook para que sea visible en la parte inferior
panel_con_pestanas.pack(expand=True, fill='both', padx=10, pady=10, side="bottom")


# Iniciar el bucle principal de la aplicación
ventana.mainloop()