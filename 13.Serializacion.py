'''
SERIALIZACION: consiste en guardar en un fichero externo por ejemplo
una coleccion un diccionario o includo un objeto, pero la particularidad
es que lo vamos a guardar en un fichero externo codificado en codigo 
binario. El objetivo puede ser diversa, si por ejemplo queremos distribuir 
un objeto que hemos construido por internet viene muy bien que este en
binario, o en una base de datos. 

Para poder realizar esto necesitamos hacer uso de una biblioteca llamada 
Pickle con los metodos:

-dump(): volcado de datos al fichero binario externo
-load(): carga de los datos del fichero binario externo

'''

import pickle

lista_nombre=["Pedro","Ana","Maria","Luis"]

#Creamos el fichero externo con acceso de escritura binario
fichero_binario = open("lista_nombres_binario","wb")

# Volcado de la lista a ese fichero
pickle.dump(lista_nombre,fichero_binario)

# Cerramos el fichero
fichero_binario.close()

# Y eliminamos de la memoria
del(fichero_binario)

# ----------------------------------------------
# Ahora queremos rescatar la informacion de ese fichero binario
fichero = open("lista_nombres_binario","rb")
lista = pickle.load(fichero)
print(lista)