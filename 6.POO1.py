'''
Clase: Modelo donde se redactan las caracteristicas comunes de un objeto o grupo de objetos
Instancia: Es un objeto perteneciente a una clase 
Encapsulacion: ocultar los detalles internos de cómo funciona una clase y solo permitir 
el acceso a través de una interfaz bien definida. Envolver los datos (variables) y los 
métodos (funciones) que operan en esos datos en una sola unidad. Esto se logra mediante el 
uso de modificadores de acceso, como públicos, privados y protegidos:

    Público (public): Los miembros públicos de una clase son accesibles desde cualquier parte 
    del programa. Estos miembros son típicamente métodos que se utilizan para interactuar con 
    los datos encapsulados de una manera controlada.

    Privado (private): Los miembros privados de una clase solo son accesibles dentro de la propia 
    clase. Esto significa que otros objetos no pueden acceder directamente a estos miembros. La 
    encapsulación se utiliza para ocultar la implementación interna de la clase y proteger los 
    datos de modificaciones no autorizadas.

    Protegido (protected): Los miembros protegidos de una clase son similares a los miembros 
    privados, pero también son accesibles por las subclases (clases que heredan de la clase base). 
    Esto permite un cierto nivel de acceso controlado para las clases derivadas.

'''

# Clase capaz de construir coches
class Coche():
    # Caracteristicas propias de la clase coche

    # Constructor
    def __init__(self):
        # Encapsulamos las variables para que no se pueda modificar con __
        self.__largo = 250
        self.__ancho = 250
        self.__ruedas = 4
        self.__enMarcha = False

    #Metodos
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo = self.__chequeoInternoInicial()
        
        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"

    def mostrarInformacion(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__ancho, " y un largo de ", self.__largo)

    # Este es un metodo accesibel desde fuera y no deberia ser asi tan solo se deberia usar dentro de la 
    # clase por ello debemos encapsularlo igual que con las variables __
    def __chequeoInternoInicial(self):
        print("*** Realizando el chequeo Interno ***")
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "cerradas"

        if(self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "cerradas"):
            return True
        else:
            return False
        
# COMIENZO DEL PROGRAMA ******************************************************

miCoche = Coche()

#print(miCoche.largo)
print(miCoche.arrancar(True))
miCoche.mostrarInformacion()
