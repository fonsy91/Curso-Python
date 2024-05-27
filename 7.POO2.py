'''
Herencia: permite a una clase heredar atributos y métodos de otra clase. Esto significa 
que una clase puede extender la funcionalidad de otra clase reutilizando su código existente.
Ademas python tiene herencia multiple es decir que una clase puede heredar de varias clases

super(): esta funcion halla donde la coloques en tu codigo va a llamar al metodo de la clase 
padre 

isinstance(): nos dice si es una instancia o no

'''

#Super clase o clase padre
class Vheiculo():
    # Constructor
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelerar=False
        self.frenar=False

    # Metodos
    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True
    
    def InformacionEstado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelerar,
              "\nFrenar: ", self.frenar)

# Clase que hereda de la clase padre Vheiculos
class Furgoneta(Vheiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

# Clase que hereda de la clase padre Vehiculos
class Moto(Vheiculo):
    caballito = ""

    def hacerCaballito(self):
        self.caballito = "Voy haciendo el caballito"
    
    # Sobreescribimos el metodo estado
    def InformacionEstado(self):
        print("Marca: ",self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelerar,
              "\nFrenar: ", self.frenar, "\n", self.caballito)

# Clase que hereda de la super clase Vheiculo y ademas llama al constructo 
# de su padre para poder usarlo y crear objetos con esos parametros
class VElectrico(Vheiculo):
    def __init__(self, marca, modelo):
        # Llamaos al constructor de la clase padre
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

# Python nos permite heredar de diferentes clases herencia multiple
# Pero siempre se le da preferencia a la primera clase que indiques en los
# parentesis
class BicicletaElectrica(VElectrico, Vheiculo):
    pass


# COMIENZO DEL PROGRAMA PRINCIPAL **********************++***********************
miMoto = Moto("HONDA","CBR")
miMoto.hacerCaballito()
miMoto.InformacionEstado()

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.InformacionEstado()
print(miFurgoneta.carga(True))

miBici = BicicletaElectrica("Orbea", "V5567")
miBici.InformacionEstado()

#VAMOS POR ESTE VIDEO
# https://www.youtube.com/watch?v=jMQQN9OxwVc&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=30