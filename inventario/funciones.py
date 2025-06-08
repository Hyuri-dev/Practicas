import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import json

CONFIG_FILE = "config.json"

def cargar_allegri(ruta_archivo = None):
    # Si se proporciona una ruta, la usamos; si no, intentamos recuperar la última ruta usada o una ruta por defecto
    ruta_a_cargar = ruta_archivo
    if ruta_archivo is None:
        # Intentamos obtener la última ruta guardada en el archivo de configuración
        ultima_ruta = obtener_ultima_ruta()
        # Si existe una última ruta y el archivo existe en esa ruta, la usamos
        if ultima_ruta and os.path.exists(ultima_ruta):
            ruta_a_cargar = ultima_ruta
            print(f"Cargando inventario desde la ruta: {ruta_a_cargar}")
        else:
            # Si no hay última ruta válida, usamos la ruta por defecto
            ruta_a_cargar = os.path.join("assets", "files", "inventario.xlsm")
            print(f"Cargando inventario desde la ruta por defecto: {ruta_a_cargar}")
    try:
        # Intentamos leer el archivo de Excel en la hoja "inventario"
        df_inventario = pd.read_excel(ruta_a_cargar, sheet_name="inventario")
        # Extraemos las columnas relevantes y las convertimos en una lista de tuplas
        datos = list(df_inventario[['PRODUCTOS ALLEGRI', 'TIPO ALLEGRI', 'CANTIDAD ALLEGRI']].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        # Si ocurre un error al leer el archivo, lo mostramos y devolvemos una lista vacía
        print(f"Error al cargar el archivo {ruta_a_cargar}:  {e}")
        return []

def seleccionar_archivo ():
    root = tk.Tk()
    root.withdraw()
    #Creamos un filedialog para buscar el archivo
    ruta_seleccionada = filedialog.askopenfilename(title="Seleccione un archivo de excel", filetypes=[("Archivos de excel", "*.xlsx *.xlsm *.xls"),("Todos los archivos","*.*")] )
    
    #creamos la logica para ver que hace el programa si se selecciona un archivo
    if ruta_seleccionada:
        guardar_ultima_ruta = (ruta_seleccionada) # si se ha seleccionado el archivo entonces guardamos la ruta en una variable
        datos_cargados = cargar_allegri(ruta_seleccionada) # Cargamos los datos al la funcion donde se carga la informacion
        print(datos_cargados[:5])
        return datos_cargados
    else:
        print("Seleccion de archivos cancelada")
        return[]

def guardar_ultima_ruta(ruta):
    """Guarda la ultima ruta del archivo seleccionado en un json para recordarla cada vez que abra el programa"""
    
    with open (CONFIG_FILE, "w") as f: # Abrimos el archivo en modo escritura para guardar la ruta en un json
        json.dump({"ultima_ruta_inventario": ruta}, f)
        print(f"Ultima ruta: {ruta}")

def obtener_ultima_ruta():
    """Obtener la ultima ruta del archivo seleccionado, lo saca del json que hemos configurado en la funcion guardar ultima ruta"""
    if os.path.exists(CONFIG_FILE): #Abrimos el archivo en modo lectura para leer la informacion del json
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f) #cargamos el json
            return config.get("ultima_ruta_inventario") #retornamos la informacion que contiene para utilizarla
        return None

def accion_seleccionar ():
    root = tk.Tk()
    root.withdraw() # oculta la venta principal
    
    ruta_seleccionada = filedialog.askopenfilename(title="Selecciona el archivo de inventario",
        filetypes=[("Archivos de Excel", "*.xlsx *.xls *.xlsm")])
    
    if ruta_seleccionada:
        guardar_ultima_ruta(ruta_seleccionada)
        datos = cargar_allegri(ruta_seleccionada)
        return datos
    else:
        print("Seleccion de archivo cancelada. ")
        return []
    


def cargar_horizonte():
    try:
        df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="INVENTARIO HORIZONTE")
        datos = list(df_inventario[['PRODUCTOS HORIZONTE', 'TIPO HORIZONTE', 'CANTIDAD HORIZONTE']].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        print(f"Error: {e}")
        return []

def cargar_monaca():
    try:
        df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="INVENTARIO MONACA")
        datos = list(df_inventario[['PRODUCTOS MONACA', 'TIPO MONACA', 'CANTIDAD MONACA']].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        print(f"Error: {e}")
        return []
    

def sumar():
  try:
      df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="inventario")
      total = df_inventario['CANTIDAD ALLEGRI'].sum() # Utilizamos sum para sumar la columna cantidad del df
      return total # Retornamos la variable para poder utilzarla luego
  except Exception as e:
    print(f"error: {e}")

def contar ():
  try:
      df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="inventario")
      contar = df_inventario['PRODUCTOS ALLEGRI'].count()
      return contar
  except Exception as e:
    print(f"error: {e}")