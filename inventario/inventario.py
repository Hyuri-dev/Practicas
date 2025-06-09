import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from components import components, rutas
from styles import colors
from funciones import *

#Ventana principal
main = tk.Tk()
main.title("Inventario")
main.geometry("1280x1000")
main.resizable(False,True)
barra_menu = tk.Menu(main)
main.config(bg= colors.Colores.background)
main.configure(menu= barra_menu)

# Crear el primer menú
menu_mantenimiento = tk.Menu(barra_menu, tearoff=False)
menu_mantenimiento.add_command(label="Abrir archivo", command=accion_seleccionar)

#Agregar menu a la barra
barra_menu.add_cascade(menu=menu_mantenimiento, label="mantenimiento")

#Creamos una barra de pestañas para añadir el inventario de novo
panel_pestañas = ttk.Notebook(main)

#Creamos la pestaña para el inventario de novo
pestaña_inventario_novo = ttk.Frame(panel_pestañas)

panel_pestañas.add(pestaña_inventario_novo, text="Inventario Novo")
panel_pestañas.grid(row= 5, column= 0 , sticky="ew", padx= 20 , pady= 10)

title_novo = tk.Label(pestaña_inventario_novo, text="Inventario Novo europa")
title_novo.pack()


#Expandimos la columna 0 de main
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure(2, weight=1)


#Frames (espacio y secciones del programa)
#--------------- navbar --------------- 
menu_frame = tk.Frame(main, bg=colors.Colores.background, width= 1280, height= 50)
menu_frame.grid(row= 0 , column=0, sticky="ew")
menu_frame.propagate(False)

logo_path = rutas.Rutas.logo_tipo
logo = Image.open(logo_path)
logo = ImageTk.PhotoImage(logo)

logo_diacenca = tk.Label(menu_frame, image=logo, bg=colors.Colores.background)
logo_diacenca.grid(row=0, column=0, sticky="w", padx= 35, pady= 10)

#--------------- stock information --------------- 
frame_info_inventory = tk.Frame(main, bg=colors.Colores.background, width=1280, height=110)
frame_info_inventory.grid(row=2, column=0)
frame_info_inventory.propagate(False)

# Configuramos 3 columnas para el frame de información
frame_info_inventory.grid_columnconfigure(0, weight=0)  # Primera card
frame_info_inventory.grid_columnconfigure(1, weight=1)  # Espaciador flexible
frame_info_inventory.grid_columnconfigure(2, weight=0)  # Imagen a la derecha

card_path1 = components.Cards.card_path
card1 = Image.open(card_path1)
card1 = ImageTk.PhotoImage(card1)

# first card
card_total_products = tk.Label(frame_info_inventory, image=card1, text=f"Total Productos: \n \n {contar()}" , bg=colors.Colores.background ,fg=colors.Colores.font_color, compound="center", font=("Arial", 20 ,"bold"))
card_total_products.grid(row=0, column=0, padx=10, pady=10, sticky="w")

#Third card
card_total_stock = tk.Label(frame_info_inventory, image=card1,  text=f"Low stock items: \n \n" ,bg=colors.Colores.background,fg=colors.Colores.font_color, compound="center", font=("Arial", 20, "bold"))
card_total_stock.grid(row=0, column=2, padx=10, pady=10, sticky="e")

#Second card
card_total_low_stock_items = tk.Label(frame_info_inventory, image=card1, text=f"Total stock: \n \n {sumar()}" , bg=colors.Colores.background, fg=colors.Colores.font_color, compound="center", font=("Arial", 20, "bold" ))
card_total_low_stock_items.grid(row=0, column=1, padx=10, pady=10, sticky="w")

#--------------- ---------------- 

#text's
title = tk.Label(main, text="Inventario", font=("Arial", 30, "bold"))
title.config(bg=colors.Colores.background,fg="Black")
title.grid(row= 1, column= 0, sticky="w", padx= 170, pady= 45)

#----- logos productos ------

frame_logos = tk.Frame(main, width=1280, height= 120 ,background=colors.Colores.background)
frame_logos.grid(row= 3, column= 0, sticky="ew", pady= 10)
frame_logos.grid_propagate(False)


#Logo allegri
allegri_logo_path = rutas.Rutas.allegri_logo
allegri_logo = Image.open(allegri_logo_path)
allegri_logo = ImageTk.PhotoImage(allegri_logo)

frame_allegri_logo = tk.Frame(frame_logos, width= 325 , height= 300, background=colors.Colores.background)
frame_allegri_logo.grid(row= 0 , column= 0, padx= 100)
frame_allegri_logo.grid_propagate(False)

logo_allegri = tk.Label(frame_allegri_logo, image=allegri_logo, bg=colors.Colores.background)
logo_allegri.grid(row= 0, column= 0, sticky="e", padx= 60)

#Logo Horizonte
horizonte_logo_path = rutas.Rutas.horizonte_logo
horizonte_logo = Image.open(horizonte_logo_path)
horizonte_logo = ImageTk.PhotoImage(horizonte_logo)

logo_horizonte = tk.Label(frame_logos, image=horizonte_logo, bg=colors.Colores.background)
logo_horizonte.grid(row = 0 , column= 1, sticky="en",padx= 35 , pady= 10)

#Logo monaca
monaca_logo_path = rutas.Rutas.monaca_logo
monaca_logo = Image.open(monaca_logo_path)
monaca_logo = ImageTk.PhotoImage(monaca_logo)

logo_monaca = tk.Label(frame_logos, image=monaca_logo ,bg=colors.Colores.background)
logo_monaca.grid(row = 0 , column= 2, sticky="en",padx= 85 , pady= 45)

#Frame horizontal
frame_horizontal = tk.Frame(main,bg=colors.Colores.background)
frame_horizontal.grid(row= 4 , column= 0, padx= (65,50) , pady= 10, sticky="ew")
frame_horizontal.grid_columnconfigure(0 , weight=1)
frame_horizontal.grid_columnconfigure(1 , weight=1)
frame_horizontal.grid_columnconfigure(2 , weight=1)


#first frame
frame_products1 = tk.Frame(frame_horizontal, width= 320, height= 400, bg=colors.Colores.background)
frame_products1.grid(row=0 , column= 0,padx=(35 ,35), sticky="nsew")
frame_products1.grid_propagate(False) # Evitamos que se propague y el frame se ajuste segun a las medidas establecidas

#first Treeview para Allegri
columns = ("Producto", "Tipo", "Cantidad")

scroll_allegri = tk.Scrollbar(frame_products1, orient="vertical")
listado_allegri = ttk.Treeview(frame_products1, columns=columns, show="headings", height=contar_allegri(), yscrollcommand=scroll_allegri.set)
scroll_allegri.config(command=listado_allegri.yview)

listado_allegri.heading("Producto" , text="Producto")
listado_allegri.heading("Tipo", text="Tipo")
listado_allegri.heading("Cantidad" , text="Cantidad")
listado_allegri.grid(row=0, column=0, sticky="nsew", pady=(2,0), ipadx=80)
scroll_allegri.grid(row=0, column=1, sticky="ns")

listado_allegri.column("Producto", width=150)
listado_allegri.column("Tipo", anchor="center", width=5)
listado_allegri.column("Cantidad", anchor="center", width=10)


#Second treeview para Horizonte
frame_products2 = tk.Frame(frame_horizontal, width=320, height=400, bg=colors.Colores.background)
frame_products2.grid(row=0, column=1, sticky="nsew", padx=(0, 35))
frame_products2.grid_propagate(False)
frame_products2.grid_rowconfigure(0, weight=1)
frame_products2.grid_columnconfigure(0, weight=1)

scroll_horizonte = tk.Scrollbar(frame_products2, orient="vertical")
listado_horizonte = ttk.Treeview(frame_products2, columns=columns, show="headings", height= contar_horizonte(), yscrollcommand=scroll_horizonte.set)
scroll_horizonte.config(command=listado_horizonte.yview)

listado_horizonte.heading("Producto", text="Producto")
listado_horizonte.heading("Tipo", text="Tipo")
listado_horizonte.heading("Cantidad", text="Cantidad")
listado_horizonte.grid(row=0, column=0, sticky="nsew", pady=(2,0), ipadx=80)
scroll_horizonte.grid(row=0, column=1, sticky="ns")

listado_horizonte.column("Producto", width=150)
listado_horizonte.column("Tipo", anchor="center", width=5)
listado_horizonte.column("Cantidad", anchor="center", width=10)

#Third treeview para Monaca
frame_products3 = tk.Frame(frame_horizontal, width=320, height=400, bg=colors.Colores.background)
frame_products3.grid(row=0, column=2, sticky="nsew")
frame_products3.grid_propagate(False)
frame_products3.grid_rowconfigure(0, weight=1)
frame_products3.grid_columnconfigure(0, weight=1)

scroll_monaca = tk.Scrollbar(frame_products3, orient="vertical")
listado_monaca = ttk.Treeview(frame_products3, columns=columns, show="headings", height=contar_monaca(), yscrollcommand=scroll_monaca.set)
scroll_monaca.config(command=listado_monaca.yview)

listado_monaca.heading("Producto", text="Producto")
listado_monaca.heading("Tipo", text="Tipo")
listado_monaca.heading("Cantidad", text="Cantidad")
listado_monaca.grid(row=0, column=0, sticky="nsew", pady=(2,0), ipadx=80)
scroll_monaca.grid(row=0, column=1, sticky="ns")

listado_monaca.column("Producto", width=150)
listado_monaca.column("Tipo", anchor="center", width=5)
listado_monaca.column("Cantidad", anchor="center", width=10)

#Cargamos los datos del excel
datos_allegri = cargar_allegri()
datos_horizonte = cargar_horizonte()
datos_monaca = cargar_monaca()

#Insertamos los datos en el treeview
for fila in datos_allegri:
    listado_allegri.insert("", "end", values=fila)

for fila in datos_horizonte:
    listado_horizonte.insert("", "end" , values=fila)

for fila in datos_monaca:
    listado_monaca.insert("", "end" , values=fila)


main.mainloop()
