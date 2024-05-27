
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