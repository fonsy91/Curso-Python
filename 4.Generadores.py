'''
GENERADORES

Son estructuras que extraen valores de una funcion y se almacenan 
en objetos iterables (que se pueden recorrer). Estos valores se almacenan 
de uno en uno. Cada vez que un generador almacena un valor, este permanece 
en un estado de pausa hasta que se solicita el siguiente. Esta 
caracteristica se conoce como "suspension de estado"

Ventajas respecto a una funcion: son mas eficientes, utiles con listas de 
valores infinitos, 

'''

# Como por ejemplo crear una funcion que devuelva una lista de numeros pares
def generaPares(limite):
    num = 1
    while num <= limite:
        yield num*2
        num = num+1

# variable donde guardamos los valores
devuelvePares = generaPares(10)

# Mostramos los elementos
#for i in devuelvePares:
#    print(i)

# Si queremos que nos devuelva de uno en un usamos next
print(next(devuelvePares))
print(next(devuelvePares))

#yield from: 
# Un astericos delante del argumento de una funcion le indicamos 
# al programa que va a recibir un numero indeterminado de elementos y
# ademas esos argumentos son en forma de tupla
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao") 
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

# Si queremos acceder a las letras de cada uno de los elementos usamos 
# bucles anidados