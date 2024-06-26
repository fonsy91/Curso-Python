'''
Expresiones regulares: son como una especie de mini lenguaje de programacion 
dentro de otro lenguaje de programacion. Son una secuencia de caracteres 
que forman un patron de busqueda. Ejemplos: buscar un texto que se ajusta 
a un formato determinado (correo electronico), buscar si existe o no una 
cadena de caracteres dentro de un texto, contar el numero de coincidencias 
dentro de un texto etc... 
'''

import re

cadena = "Vamos a aprender expresiones regulares" 
print(re.search("aprender",cadena)) # <re.Match object; span=(8, 16), match='aprender'>
print(re.search("aprenderrrrr",cadena)) # None

textoBuscar = "expresiones"

if re.search(textoBuscar,cadena) is not None:
    print("He ncontrado el texto")
else:
    print("No he encontrado el texto")

# Otros metodos
textoEncontrado = re.search(textoBuscar,cadena)
# Nos devuelve el numero de caracter donde comienza la palabra
print(textoEncontrado.start())
# Nos devuelve el numero de caracter donde acaba la palabra
print(textoEncontrado.end())
# Nos devuelve ambos donde comienza y donde acaba en forma de tupla
print(textoEncontrado.span())
# Nos devuelve todas las coincidencias si hay palabras iguales
print(re.findall(textoBuscar,cadena))

'''
En las expresiones regulares tambien existen los metacaracteres 

'''

listaNombres = ["Ana Gómez","María Martín","Sandra Lopez","Santiago Martín"]

# Obtenemos una lista cuyo nombre sea Ana con este caracter ^ busca la palabra 
# que comienze con ese caracter
for elemento in listaNombres:
    if re.findall("^Ana", elemento):
        print(elemento)

# Tambien podemos usar el $ para buscar la palabra del final
for elemento in listaNombres:
    if re.findall("Lopez$", elemento):
        print(elemento)

'''
Expresiones regulares los rangos nos permiten buscar elementos dentro de
una lista que contenga un rango de caracteres, de numeros
'''

# '[o-t]' con esto indicamos que dentro de una lista nos devuelva 
# todos aquellos cuyo interior hay un rango de letras comprendido entre la o y la t
for elemento in listaNombres:
    if re.findall('[o-t]', elemento):
        print(elemento)

# '^[O-T]' nos devuelve todos los nombres que empiecen por O o T
for elemento in listaNombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)

# Ma[0-3] nos devuelve todas las palabras que empiecen po Ma y que despues tengan
# un numero seguido de 0, 1 o 3
