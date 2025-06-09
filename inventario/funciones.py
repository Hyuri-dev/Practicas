import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import json

CONFIG_FILE = "config.json"

def cargar_datos_excel(sheet_name, columnas, ruta_archivo=None):
    """
    Carga datos de un archivo Excel dado el nombre de la hoja y las columnas a extraer.
    Si no se proporciona ruta, permite seleccionar el archivo y guarda la última ruta usada.
    """
    ruta_a_cargar = ruta_archivo
    if ruta_archivo is None:
        ultima_ruta = obtener_ultima_ruta()
        if ultima_ruta and os.path.exists(ultima_ruta):
            ruta_a_cargar = ultima_ruta
            print(f"Cargando desde la última ruta: {ruta_a_cargar}")
        else:
            ruta_a_cargar = os.path.join("assets", "files", "inventario.xlsm")
            print(f"Cargando inventario desde la ruta por defecto: {ruta_a_cargar}")
    try:
        df = pd.read_excel(ruta_a_cargar, sheet_name=sheet_name)
        datos = list(df[columnas].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        print(f"Error al cargar el archivo {ruta_a_cargar}:  {e}")
        return []

# Wrappers para cada hoja

def cargar_allegri(ruta_archivo=None):
    """
    Carga los datos de Allegri filtrando filas vacías o con NaN en el producto.
    """
    datos = cargar_datos_excel(
        sheet_name="inventario",
        columnas=['PRODUCTOS ALLEGRI', 'TIPO ALLEGRI', 'CANTIDAD ALLEGRI'],
        ruta_archivo=ruta_archivo
    )
    # Filtrar filas donde el producto es vacío o NaN
    datos_filtrados = [fila for fila in datos if fila[0] and str(fila[0]).strip().lower() != 'nan']
    return datos_filtrados

def cargar_horizonte(ruta_archivo=None):
    return cargar_datos_excel(
        sheet_name="INVENTARIO HORIZONTE",
        columnas=['PRODUCTOS HORIZONTE', 'TIPO HORIZONTE', 'CANTIDAD HORIZONTE'],
        ruta_archivo=ruta_archivo
    )

def cargar_monaca(ruta_archivo=None):
    return cargar_datos_excel(
        sheet_name="INVENTARIO MONACA",
        columnas=['PRODUCTOS MONACA', 'TIPO MONACA', 'CANTIDAD MONACA'],
        ruta_archivo=ruta_archivo
    )

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
    


def sumar(ruta_archivo=None):
    """
    Suma todas las cantidades de los tres inventarios: Allegri, Horizonte y Monaca, ignorando valores vacíos o NaN.
    """
    total = 0
    # Allegri
    datos_allegri = cargar_datos_excel(
        sheet_name="inventario",
        columnas=['CANTIDAD ALLEGRI'],
        ruta_archivo=ruta_archivo
    )
    total += sum([fila[0] for fila in datos_allegri if isinstance(fila[0], (int, float)) and pd.notna(fila[0])])
    # Horizonte
    datos_horizonte = cargar_datos_excel(
        sheet_name="INVENTARIO HORIZONTE",
        columnas=['CANTIDAD HORIZONTE'],
        ruta_archivo=ruta_archivo
    )
    total += sum([fila[0] for fila in datos_horizonte if isinstance(fila[0], (int, float)) and pd.notna(fila[0])])
    # Monaca
    datos_monaca = cargar_datos_excel(
        sheet_name="INVENTARIO MONACA",
        columnas=['CANTIDAD MONACA'],
        ruta_archivo=ruta_archivo
    )
    total += sum([fila[0] for fila in datos_monaca if isinstance(fila[0], (int, float)) and pd.notna(fila[0])])
    return total

def contar(ruta_archivo=None):
    """
    Cuenta la cantidad de productos de los tres inventarios: Allegri, Horizonte y Monaca.
    """
    total = 0
    # Allegri
    datos_allegri = cargar_datos_excel(
        sheet_name="inventario",
        columnas=['PRODUCTOS ALLEGRI'],
        ruta_archivo=ruta_archivo
    )
    total += len([fila for fila in datos_allegri if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    # Horizonte
    datos_horizonte = cargar_datos_excel(
        sheet_name="INVENTARIO HORIZONTE",
        columnas=['PRODUCTOS HORIZONTE'],
        ruta_archivo=ruta_archivo
    )
    total += len([fila for fila in datos_horizonte if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    # Monaca
    datos_monaca = cargar_datos_excel(
        sheet_name="INVENTARIO MONACA",
        columnas=['PRODUCTOS MONACA'],
        ruta_archivo=ruta_archivo
    )
    total += len([fila for fila in datos_monaca if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    return total

def contar_allegri(ruta_archivo=None):
    """
    Cuenta la cantidad de productos válidos (no vacíos ni NaN) en la columna 'PRODUCTOS ALLEGRI'.
    Útil para definir la altura del Treeview.
    """
    datos_allegri = cargar_datos_excel(
        sheet_name="inventario",
        columnas=['PRODUCTOS ALLEGRI'],
        ruta_archivo=ruta_archivo
    )
    contar = len([fila for fila in datos_allegri if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    return contar

def contar_horizonte(ruta_archivo=None):
    """
    Cuenta la cantidad de productos válidos (no vacíos ni NaN) en la columna 'PRODUCTOS ALLEGRI'.
    Útil para definir la altura del Treeview.
    """
    datos_allegri = cargar_datos_excel(
        sheet_name="INVENTARIO HORIZONTE",
        columnas=['PRODUCTOS HORIZONTE'],
        ruta_archivo=ruta_archivo
    )
    contar = len([fila for fila in datos_allegri if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    return contar

def contar_monaca(ruta_archivo=None):
    """
    Cuenta la cantidad de productos válidos (no vacíos ni NaN) en la columna 'PRODUCTOS ALLEGRI'.
    Útil para definir la altura del Treeview.
    """
    datos_allegri = cargar_datos_excel(
        sheet_name="INVENTARIO MONACA",
        columnas=['PRODUCTOS MONACA'],
        ruta_archivo=ruta_archivo
    )
    contar = len([fila for fila in datos_allegri if fila[0] and str(fila[0]).strip().lower() != 'nan'])
    return contar