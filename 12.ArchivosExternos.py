'''
El objetivo de trabajar con archivos externos, tiene la posibilidad 
de guardar los datos que has estado utilizando para que no se pierdan
hay dos alternativas:

1º: Guarda esos datos en archivos externos 
2º: Trabajo con BBDD

Primero trabajaremos con la alternativa primera y mas adelante con bases 
de datos. Para archivos externos hay archivos de muchos tipos como 
binarios, de texto plano...

Vamos a ver como guardar informacion en archivos de texto plano las 
fases necesarias son:

1º: Creacion
2º: Apertura
3º: Manipulacion
4º: Cierre

'''

from io import open

# PROGRAMA PRINCIPAL *******************************************

# Abrimos un archivo y el modo en que queremos abrirlo puede ser
# en modo lectura, escritura, append (para modificar)
archivo_texto = open("archivo.txt","w")

frase = "Hola soy Alfonso \n programo python y acabo de escribir esto"

# Incluimos la frase en el archivo
archivo_texto.write(frase)

# Cerramos el archivo
archivo_texto.close()

# Si queremos abrir un archivo en modo lectura
archivo_texto_lectura = open("archivo.txt","r")
# texto = archivo_texto_lectura.read()

# Tambien existe el metodo readlines(): lee la informacion almacenada 
# en el archivo linea por linea y almacenar esa informacion en una lista
textoLinea = archivo_texto_lectura.readlines()

archivo_texto_lectura.close()

# print(texto)
print(textoLinea)

# Tambien podemos acceder a las posiciones de la lista del texto plano 
# creado con readlines()
print(textoLinea[0])

# Si queremos agregarle nuevo contenido al archivo usamos el append 
archivo_texto_modificacion = open("archivo.txt","a")
archivo_texto_modificacion.write("\nAgregamos texto con append")
archivo_texto_modificacion.close()

# PARTE DOS ***********************************************************
# Tambien se pueden manipular archivos externos usando punteros en texto
archivo_texto_puntero = open("archivoPuntero.txt","w")
frasePuntero = "Hola estamos usando punteros en python \n y soy Alfonso"
archivo_texto_puntero.write(frasePuntero)
archivo_texto_puntero.close()

archivo_texto_puntero_lectura = open("archivoPuntero.txt", "r")
# textoPuntero = archivo_texto_puntero_lectura.read()
# print(archivo_texto_puntero_lectura.read())
# print(textoPuntero)

# Si no indiamos nada el puntero se situa al principio del archivo cuando creamos
# pero cuando leemos se situa al final. Para situar el puntero en una posicion 
# expecifica usamos el metodo seek() nos va a pedir un numero de caracteres que 
# va a ser donde se situe el puntero

# Lee el archivo y se situa el puntero al final
print(archivo_texto_puntero_lectura.read())
# Despues lo volvemos a situar al principio
archivo_texto_puntero_lectura.seek(0)
# Se volvera a imprimir el mismo texto
print(archivo_texto_puntero_lectura.read())

# Tambien se pueden crear archivos en modo escritura y lectura a la vez:
# archivo_texto_puntero = open("archivoPuntero.txt","r+")