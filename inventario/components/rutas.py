import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Aqui encontraras las rutas de las imagenes que utilizo en este proyecto

class Rutas:
    logo_tipo = os.path.join(BASE_DIR, "assets","images","logo_diacenca.png")
    allegri_logo = os.path.join(BASE_DIR,"assets", "images", "allegri_logo.png")
    horizonte_logo = os.path.join(BASE_DIR,"assets", "images", "horizonte_logo.png")
    monaca_logo = os.path.join(BASE_DIR,"assets", "images", "monaca_logo.png")

