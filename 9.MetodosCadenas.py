'''
Python considera a las cadenas de caracteres (palabras) frases, letras objetos
de tipo String algunos son: 

upper(): convierte en mayusculas todas las letras
lower(): convierte en minusculas todlas las letras
capitalize(): pone en mayusculas solo la primera letra
count(): cuenta cuantas veces aparece una letra o una cadena dentro de un texto
find(): representa el indice la posicion en la cual aparece un caracter o un grupo dentro de un texto
isdigit(): devuelve un booleano diciendonos si el valor es in digito o no lo es
isalum(): comprueba sin son alfanumericos
isalpha(): comprobar si solo hay letras
split(): split separa por palabras utilizando espacios 
strip(): borrar los espacios sobrantes al principio y al final
replace(): cambia una palabra o una letra por otra dentro de un string
rfind(): representa el indice de un caracter pero este lo hace contando desde atras dentro del string

Docuemntacion de python: https://pyspanishdoc.sourceforge.net/
Docuemntacion cadenas: https://pyspanishdoc.sourceforge.net/lib/string-methods.html

'''

nombreUsuario = input("Introduce nombre de usuario: ")

# print("El nombre es: ", nombreUsuario.upper())
# print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())

numero = 20
print(str(numero).isdigit())

# Elimina los espacios en blanco al inicio y al final de la cadena.
texto = "   Hola Mundo   "
print(texto.strip())   # "Hola Mundo"
print(texto.lstrip())  # "Hola Mundo   "
print(texto.rstrip())  # "   Hola Mundo"

# Reemplaza todas las ocurrencias de un subcadena por otra.
texto = "Hola Mundo"
print(texto.replace("Hola", "Adiós"))  # Adiós Mundo

# Divide la cadena en una lista usando el separador especificado.
texto = "Hola Mundo"
print(texto.split())      # ['Hola', 'Mundo']
print(texto.split('o'))   # ['H', 'la Mund', '']

# Une los elementos de un iterable con la cadena especificada como separador.
lista = ['Hola', 'Mundo']
print(' '.join(lista))  # Hola Mundo
print('-'.join(lista))  # Hola-Mundo

# Verifica si la cadena comienza o termina con el prefijo o sufijo especificado.
texto = "Hola Mundo"
print(texto.startswith("Hola"))  # True
print(texto.endswith("Mundo"))   # True

# Encuentra la posición de la primera o última aparición de la subcadena.
texto = "Hola Mundo"
print(texto.find("Mundo"))   # 5
print(texto.rfind("o"))      # 9

# Cuenta el número de veces que aparece la subcadena en la cadena.
texto = "Hola Mundo Mundo"
print(texto.count("Mundo"))  # 2

# Convierte las letras mayúsculas a minúsculas y viceversa.
texto = "Hola Mundo"
print(texto.swapcase())  # hOLA mUNDO