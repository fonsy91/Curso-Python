# Si queremos importar todo el modulo
from Modulos import FuncionesMatematicas

# Si queremos importar solo una funcion 
#from Modulos import sumar

# Si quires importar todo y solo usar el nombre del metodo, variable, constante...
from Modulos.FuncionesMatematicas import *

# Importamos el modulo de clases
from Modulos.ClasesVehiculos import *


'''
Modulos: es un archivo que contiene definiciones y declaraciones de python
como funciones, clases, variables u otros modulos. Esto te permite organizar y 
reutilizar el codigo.

'''

# Hemos creado un archivo (modulo) de Funciones matematicas en la
# carpeta Modulos la cual vamos a utilizar 

# Si queremos importar todo el modulo
FuncionesMatematicas.sumar(4,4)

# Si quires importar todo y solo usar el nombre del metodo, variable, constante...
restar(4,2)

# Utilizando el modulo de clase Vehiculos
miCoche = Vheiculo("MAZDA","XC5")
miCoche.InformacionEstado()