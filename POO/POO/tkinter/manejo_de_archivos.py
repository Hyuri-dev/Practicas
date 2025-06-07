#para manejar archivos se suelen utilizar diferentes metodos o modos de acceso
# Sólo lectura ('r'): Este modo abre los ficheros de texto sólo para lectura. El inicio del fichero es donde se encuentra el manejador. Se produce un error de E/S si el fichero no existe. Este es también el modo por defecto para abrir ficheros.

# Lectura y escritura ('r+'): Este método abre el fichero tanto para lectura como para escritura. Si el fichero no existe, se produce un error de E/S. Si el fichero no existe, se produce un error de E/S.

# Sólo escritura ('w'): Este modo abre el fichero sólo para escritura. Los datos de los ficheros existentes se modifican y sobrescriben. El inicio del fichero es donde se encuentra el manejador. Si el fichero no existe ya en la carpeta, se crea uno nuevo.

# Escritura y lectura ('w+'): Este modo abre el fichero tanto para lectura como para escritura. El texto se sobrescribe y se borra de un fichero existente. El inicio del fichero es donde se encuentra el manejador.

# Sólo añadir ('a'): Este modo permite abrir el fichero para escribir. Si el fichero aún no existe, se crea uno nuevo. El manejador se coloca al final del fichero. Los datos recién escritos se añadirán al final, a continuación de los datos escritos anteriormente.

# Añadir y leer ('a+'): Este método permite leer y escribir en el fichero. Si el fichero no existe, se crea uno. El manejador se coloca al final del fichero. El texto recién escrito se añadirá al final, a continuación de los datos escritos anteriormente.

#con open(nombre archivo , "x") abrira el archivo si existe pero si no existe entonces creara el archivo
#Hay diferentes funciones/codigos para abrir un archivo a continuacion te dejo los siguientes y que caracteristica tienen.

#"x" - Crear: este comando creará un nuevo archivo si y sólo si no existe ya un archivo con ese nombre o, de lo contrario, devolverá un error.

# "w" - Escribir: este comando creará un nuevo archivo de texto independientemente de que exista o no un archivo en la memoria con el nuevo nombre especificado. 
# No devuelve un error si encuentra un archivo existente con el mismo nombre - en su lugar, sobrescribirá el archivo existente.

file = open("myfile", "r+")


#Escribiendo texto en un archivo

#Para escribir en el archivo que se acaba de abrir necesitaremos el uso de 2 tipos de metodos dependiendo de las necesidades que se tengan

# Metodo Write(), esta funcion inserta el texto que queremos escribir en el archivo en una sola linea 

# file.write("Hola, aqui te deja un saludo hyuri.dev")

#Metodo writelines(), Esta función inserta múltiples cadenas al mismo tiempo. Se crea una lista de elementos de cadena y,
# a continuación, se añade cada cadena al archivo de texto.

# file.writelines(["aca estariamos" , "seccionando", "los textos \n"]) 

saludo = " Hola, te envia un saludo hyuri.dev \n"
L = ["Esto es  un texto \n", "acompañado de saltos de linea \n", "y nuevo texto \n"]

file.write(saludo)
file.writelines(L)
file.close()

#Leyendo archivos 

#Para leer archivos de texto tenemos 3 metodos que son los siguientes:

# Metodo read()

#Esta funcion devuelve los bytes leidos en formato string, si no se especifica como lo va a leer, el metodo read leera todo el archivo por completo

file = open("myfile", "r")
print(file.read())
file.close()

#Metodo readline (), Esta función lee una línea de un fichero y la devuelve como cadena. Lee como máximo n bytes para la n especificada. 
# Pero aunque n sea mayor que la longitud de la línea, no lee más de una línea.

file = open("myfile", "r")
print(file.readline())
file.close()

#Metodo writelines(), Esta función lee todas las líneas
# y las devuelve como elementos de cadena en una lista, uno por cada línea.

file = open("myfile", "r")
print(file.readlines())
print(file.readlines())
file.close()
