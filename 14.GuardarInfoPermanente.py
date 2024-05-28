'''
Guardar datos de forma permanete en ficheros ademas de 
poderse reutilziar desde cualquier proyecto o fichero

'''

import pickle

# Clase persona
class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    # Convertimos en cadena de texto la informacion de un objeto
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    
    personas = []

    # constructor
    def __init__(self):
        # abrimos fichero con permisos de agregar informacion binaria
        listaDePersonas = open("listaPersonasBinario","ab+")
        # Desplazamos el cursor al principio para luego poder leer
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    # Metodo apra agregar personas 
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasFicheroExterno()


    # Metodo para leer personas
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    # Guardar personas 
    def guardarPersonasFicheroExterno(self):
        listaDePersonas = open("listaPersonasBinario","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    # Mostrar info fichero externo
    def mostrarFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

# CLASE PRINCIPAL ****************************************************
# El objetivo es ir creando personas y que se vayan almacenando en el archivo externo

miLista = ListaPersonas()

persona1 = Persona("Sandra", "Femenino", 32)
persona2 = Persona("Luis", "Masculino", 28)
persona3 = Persona("Pedro", "Masculino", 55)

miLista.agregarPersonas(persona1)
miLista.agregarPersonas(persona2)
miLista.agregarPersonas(persona3)

miLista.mostrarPersonas()

miLista.mostrarFicheroExterno()