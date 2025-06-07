import pandas as pd
import os

def cargar_allegri():
    try:
        df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="inventario")
        datos = list(df_inventario[['PRODUCTOS ALLEGRI', 'TIPO ALLEGRI', 'CANTIDAD ALLEGRI']].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        print(f"Error: {e}")
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