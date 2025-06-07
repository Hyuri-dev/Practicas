import pandas as pd
import os

def cargar():
    try:
        df_inventario = pd.read_excel(os.path.join("assets", "files", "inventario.xlsm"), sheet_name="inventario")
        datos = list(df_inventario[['PRODUCTO', 'TIPO', 'CANTIDAD']].itertuples(index=False, name=None))
        return datos
    except Exception as e:
        print(f"Error: {e}")
        return []