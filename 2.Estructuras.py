# ESTRUCTURAS DE DATOS: LISTAS, TUPLAS Y DICCIONARIOS

#LISTAS ***************************************************
listaNombres = ["Alfonso","Juan","Laura","Maria"]
print("Mi lista es: ", listaNombres)
print(listaNombres[0])
# Mostramos un indice negativo es decir empezara a contar
# desde el -1 como el ultimo en adelante 
print(listaNombres[-1])
# Si quieres solamente una porcion de lista 
# el 0 incluye el nombre el 2 no lo incluye en este caso solo mostraria
# los nombres con los indices 0 y 1 Alfonso y Juan
# si no pones el 0 -> [:2] python lo entiende y es lo mismo que [0:2]
# Si pongo [1:2] -> pone el indice 0 y el dos lo excuye saldria por pantalla "Juan"
# Si pongo [2:] -> le estamos diciendo que acceda a los dos utimos elementos se traduce como desde el 
# indice 2 hasta el final
print(listaNombres[0:2])
print("Accediendo a los dos ultimos elementos: ", listaNombres[2:])

# Si queremos agregar un elemento a la lista utilizamos la funcion append
# esta agregara el elemento al final de la lista
listaNombres.append("Pedro")
print(listaNombres)

# Si quires introducir el elemento en un indice expecifico se usa la funcion insert
listaNombres.insert(1,"Rojelia")
print(listaNombres)

# Si quieres insertar no uno sino varios
listaNombres.extend(["Ana","Lucia","Mario"])
print(listaNombres)

#Buscar el indice de un nombre en concreto o con booleanos 
print(listaNombres.index("Alfonso"))
print("Alfonso" in listaNombres)

# Las listas en python tambien pueden almacenar diferentes tipos de 
# datos
listaVaria = ["Alfonso",5,True,8.35]
print(listaVaria)

# Eliminar un elemento de la lista
listaNombres.remove("Maria")
print(listaNombres)

# Tambien puedes eliminar el ultimo elemento de una lista con la funcion pop
listaNombres.pop()
print(listaNombres)

# Unimos dos listas en una 
listaFinal = listaNombres + listaVaria
print(listaFinal)

#TUPLAS ***************************************************
'''
Son como las listas pero con algunas restricciones 
en este caso las tuplas son inmutables no se pueden 
modificar despues de su creacion: no se pueden ni añadir elementos,
eliminar, mover. Permiten extraer elementos que serian otras tuplas 
no permite buscar elementos. La unica ventaja que tienen es que son 
mas rapidas ocupan menos espacio Formatean String y se pueden utilizarse 
como claves en un diccionario (las listas no). Las lista se muestran con
corchetes y las tuplas con parentesis
'''

tuplaCiudades = ("Madrid","Almeria","Segovia",9,1991)
print(tuplaCiudades[0])

#Podemos convertir tuplas en listas y viceversa listas en tuplas
#Tupla en lista
miLista = list(tuplaCiudades)

#Lista a tupla
miTupla = tuple(miLista)

# El metodo Count nos permite averiguar cuantas veces se repite el 
# elemento que le pases
print(miTupla.count(9))

# El metodo lenght nos permite averiguar la longitud de la tupla o lista
print(len(miTupla))

#DICCIONARIOS ***************************************************
'''
Estrucrturas de datos que nos permiten almacenar valores de diferentes
tipos e incluso listas y otros diccionarios. Se diferencian de los demas 
porque los datos almacenados van asociados a una clave, es decir se crea una
asociacion de tipo clave : valor. A la hora de guardar elementos no tienen 
ningun orden. 
'''

miDiccionario = {"España":"Madrid","Alemania":"Berlin","Italia":"Roma"}
print(miDiccionario)
print(miDiccionario["España"])

# Agreamos un valor nuevo a una clave
miDiccionario["Italia"]="Bota"

# Eliminar una valor de una clave/valor
del miDiccionario["Italia"]
print(miDiccionario)

diccionarioId = {1:"Alfonso", 2:"Juan", 3:"Lucia"}

jugadores_baloncesto = {
    23: 'Michael Jordan',
    30: 'Stephen Curry',
    3: 'LeBron James',
    11: 'Kyrie Irving',
    34: 'Shaquille O\'Neal', 
    8: 'Kobe Bryant'
}

# Se pude utilizar una tupla para asignar las claves al diccionario
tuplaClave = ("España", "Francia", "Alemania")
diccionarioValor = {tuplaClave[0]:"Madrid", tuplaClave[1]:"Paris", tuplaClave[2]:"Berlin"}
print(diccionarioValor)
# Si pones el valor de la tupla aparece el valor del diccionario
print(diccionarioValor["España"])

# Creamos un diccionario simulando una estructura de datos de una persona
diccionarioPersona = {
    "Nombre": "Juan",
    "Edad": 23,
    "DNI": "50776089T",
    "Dinero": 12345,
    "Telefonos": [915215033, 61823468],
    "Familia": {"Padre": "Alfonso", "Madre":"Juana", "Hermana":"Silvia"}
}

print(diccionarioPersona)
print(diccionarioPersona["Familia"])

# Mostramos las llaves de un diccionario
print(diccionarioPersona.keys())