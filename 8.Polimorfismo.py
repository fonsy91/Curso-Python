'''
Polimorfismo: 

'''

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


# PROGRAMA PRINCIPAL ******************************
'''
miVheiculo = Moto()
miVheiculo.desplazamiento()

miVheiculo2 = Coche()
miVheiculo2.desplazamiento()

miVheiculo3 = Camion()
miVheiculo3.desplazamiento()
'''

# En vez de usar lo anterior usamos el polimorfismo
def desplazamientoVheiculo(vehiculo):
    vehiculo.desplazamiento()

camion = Camion()
desplazamientoVheiculo(camion)


# VAMOS POR ESTE VIDEO: https://www.youtube.com/watch?v=zH0VsRuD2ok&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=33