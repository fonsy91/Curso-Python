# METODOS Y FUNCIONES ************************

import math


def evaluacion(nota):
    val = "aprobado"
    if nota < 5:
        val="suspenso"
    return val

# PROGRAMA PRINCIPAL **************************

print("Programa de evaluacion de alumnos: ")

# Introducimos una valor de nota
# NOTA: todo valor que introduccimos en el input() para python es
# considerado como un valor de texto por tanto habra que hacer un cast
# con el valor que nosotros queremos
notaAlumno = input()

# Convertirmo lo introducido en un entero
print(evaluacion(int(notaAlumno)))

'''
El metodo inpuy() permite recibir parametros es decir
que el texto de solicitacion de notas puede ir incluido 
dentro del input: edad = input("Introduce una edad: ")
'''

print("Verifiacion de acceso.")
edadUsuario = int(input("Introducce tu edad: "))

if edadUsuario < 18:
    print("No puedes pasar")
elif edadUsuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

# Concatenacion de operadores de comparacion

edad = -7

# Evalua condiciones de izquierda a derecha
if 0 < edad < 100:
    print("Edad correcta")
else: 
    print("Edad incorrecta")

# BUCLES *******************************

for i in [1,2,3]:
    print(i)

# Si queires que se ejecuten en una sola linea 
for i in ["Hola",2,"Alfonso"]:
    print(i, end=" ")

print()

# Forma de comprobacion de correo electronico
correo = "alfonso91@gmail.com"
email = False

for i in correo:
    if i == "@":
        email = True

if email == True:
    print("Email correcto")
else:
    print("Email incorrecto")

# Tambien puede recorrer el numero de veces que tu quieras, en este caso
# ssaldria HOLA 4 veces, 0,1,2,3 un total de 4 
for i in range(4):
    print("HOLA", end=" ")

print()

# Notaciones especiales con print()
# Concatenar el valor de texto print con la funcion (f) unimos textos con variables
for i in range(4):
    print(f"valor de la variable {i}")

# Tambien se puden hacer bucles personalizados de un numero a otro determinado
for i in range(3,5):
    print("Bucle determinado")

# O de cuanto en cuanto tiene que ir en este caso ira del 1 al 10 de dos en dos
for i in range(1,10,2):
    print(i)

# Para saber la longitud de un string usamos el metod len
for i in range(len("Juan")):
    print(i)

# Bucle while 
i=0

while i < 4:
    print("Ejecuta")
    i=i+1

# Uso de while para el calculo de raiz cuadrada 
numero = int(input("Introduce un numero: "))
intentos = 0
while numero < 0:
    print("No se puede hallar la raiz cuadrada de un numero negativo")
    if intentos == 2:
        print("Demasiados intentos consumidos")
        break;

    numero = int(input("Introduce un numero: "))
    if numero < 0:
        intentos=intentos+1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadarada de " + str(numero) + " es " + str(solucion))

'''
Cotinue: cuando estas en un bucle se salta una vuelta del bucle 
pass: En cuanto se le pass en el interior de un bucle nos devuelve null

Una funcionalidad de python es la de poder poner else: para un bucle 
es decir si tras todas las iteraciones no se ejecuta nada ejecutara el else
'''

for letra in "Python":
    # En este caso cuando se encuentre con la linea continue 
    # evitara esa iteracion y saldra por pantalla Pyton sin h
    if letra == "h":
        continue

    print("Viendo la letra: " + letra)