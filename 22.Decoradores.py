'''
Decoradores: Son funciones que añaden funcionalidad a otras funciones.
Una funcion decorador esta compuesta por 3 funciones (A, B y C) donde
A recibe como parametro a B y devuelve C, un decorador devuelve una funcion.
'''

# Si queremos dar funconalidad a todas las funciones que tenemos en este caso
# son solo dos pero podrian ser las que fueran pues para ello usamos una funcion
# decoradora la cual antes de sacar el resultado impriman un mensaje 

def funcionDecorador(funcion ):
    def funcionInterior():
        print("Vamos a realizar un calculo")
        funcion()
        print("Hemos terminado el calculo")
    return funcionInterior 

@funcionDecorador
def suma():
    print(15+20)

@funcionDecorador
def resta():
    print(30-10)


