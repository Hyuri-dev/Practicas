# Este archivo contiene las funcionalidades del segundo inventario#
import pandas as pd
import json
import os
import tkinter as tk
from tkinter import filedialog
from components.rutas import BASE_DIR

CONFIG_FILE = "config.json"

# Cargamos el archivo donde se encuentra el inventario#
def cargar_archivo (sheet_name , columnas, ruta_archivo = None):
  
  ruta_a_cargar = ruta_archivo
  
  if ruta_archivo is None:
    ultima_ruta = obtener_ultima_ruta()
    if ultima_ruta and os.path.exists(ultima_ruta):
      ruta_a_cargar = ultima_ruta
      print(f"Cargando desde la ultima ruta: {ruta_a_cargar}")
    else:
      ruta_a_cargar = os.path.join(BASE_DIR, "assets" , "files", "inventario.xlsm")
      print(f"Cargando desde la ruta por defecto: {ruta_a_cargar}")
  
  try:
    df = pd.read_excel(ruta_a_cargar, sheet_name= sheet_name)
    datos = list(df[columnas].itertuples(index = False, name = None))
    return datos
  except Exception as e:
    print(f"Error al cargar el archivo {ruta_a_cargar}: {e}")
    return[]

# Funciones para cargar los productos por marca

def inventario_sirena (ruta_archivo = None):
  return cargar_archivo (sheet_name= "inventario", columnas= ["VENECIANA", "TIPO VENECIANA" , "CANTIDAD VENECIANA"], ruta_archivo= ruta_archivo)

def inventario_oleica (ruta_archivo = None):
  datos = cargar_archivo(sheet_name= "inventario", columnas= ["OLEICA", "TIPO OLEICA", "CANTIDAD OLEICA"], ruta_archivo= ruta_archivo)
  
  #Filtrar para evitar valores vacios o NaN
  datos_filtrados = [fila for fila in datos if fila [0] and str(fila[0]).strip().lower() != 'nan' and fila [2] > 0]
  return datos_filtrados


def inventario_giralda (ruta_archivo = None):
  datos = cargar_archivo(sheet_name= "inventario", columnas= ["GIRALDA", "TIPO GIRALDA", "CANTIDAD GIRALDA"], ruta_archivo= ruta_archivo)

  #Filtrar para evitar valores vacios o NaN
  datos_filtrados = [fila for fila in datos if fila [0] and str(fila[0]).strip().lower() != 'nan' and fila [2] > 0]
  return datos_filtrados

# Guardar y obtener las rutas del JSON #
def guardar_ultima_ruta(ruta):
  
  with open (CONFIG_FILE, "w") as f:
    json.dump({f"Ultima_ruta_novo: {ruta}"}, f)
    print(f"Ultima ruta es: {ruta}")

def obtener_ultima_ruta ():
  if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
      config = json.load(f)
      return config.get("ultima_ruta_novo")
    return None


#Contar la cantidad de productos por marca#

# Calcular total productos veneciana

def contar_veneciana (ruta_archivo = None):
  datos_veneciana = cargar_archivo(sheet_name="inventario", columnas=["VENECIANA"], ruta_archivo= ruta_archivo)
  
  contar = len([fila for fila in datos_veneciana if fila [0] and str(fila[0]).strip().lower() != 'nan'])
  print(f'Total productos: {contar}')
  return contar





# Calcular total productos oleica

def contar_oleica(ruta_archivo = None):
  datos_oleica= cargar_archivo(sheet_name="inventario", columnas=["OLEICA"], ruta_archivo= ruta_archivo)
  
  contar = len([fila for fila in datos_oleica if fila [0] and str(fila[0]).strip().lower() != 'nan'])
  print(f'Total productos: {contar}')
  return contar





# Calcular total productos giralda
def contar_giralda (ruta_archivo = None):
  datos_giralda = cargar_archivo(sheet_name="inventario", columnas=["GIRALDA"], ruta_archivo= ruta_archivo)
  
  contar = len([fila for fila in datos_giralda if fila [0] and str(fila[0]).strip().lower() != 'nan'])
  print(f'Total productos: {contar}')
  return contar



#Operaciones para la informacion de las tarjetas

def sumar_stock_novo (ruta_archivo = None):
  
  total = 0
  
  datos_veneciana = cargar_archivo(sheet_name= "inventario", columnas=["CANTIDAD VENECIANA"], ruta_archivo=ruta_archivo)
  total += sum([fila[0] for fila in datos_veneciana if isinstance(fila[0], (int, float))and pd.notna(fila[0])])

  datos_oleica = cargar_archivo(sheet_name= "inventario", columnas=["CANTIDAD OLEICA"], ruta_archivo=ruta_archivo)
  total += sum([fila[0] for fila in datos_oleica if isinstance(fila[0], (int, float))and pd.notna(fila[0])])

  datos_giralda = cargar_archivo(sheet_name= "inventario", columnas=["CANTIDAD GIRALDA"], ruta_archivo=ruta_archivo)
  total += sum([fila[0] for fila in datos_giralda if isinstance(fila[0], (int, float))and pd.notna(fila[0])])
  print(total)
  return total

# Aviso de productos en bajo o nada de stock
def low_stock_novo (ruta_archivo = None, umbral = 5):
  total_bajo_stock = 0
  
  columnas =["CANTIDAD VENECIANA", "CANTIDAD OLEICA" , "CANTIDAD GIRALDA"]
  for columna in columnas:
    cantidades = cargar_archivo("inventario" , columna, ruta_archivo)
    
    bajo_stock = [
      cantidad for cantidad in cantidades 
      if isinstance(cantidad, (int,float)) and pd.notna and cantidad <= umbral
    ]
    total_bajo_stock += len(bajo_stock)
    print(f'productos en bajo stock: {total_bajo_stock}')
  return total_bajo_stock