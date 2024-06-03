'''
Funcion map: aplica una funcion a cada elemento de una lista iterable 
(listas, tuplas etc) devolviendo una lista con los resultados.
'''

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} euros".format(self.nombre, self.cargo, self.salario)

# Normalmente utilizamos filter para filtrar objetos
listaEmpleados = [
    Empleado("Juan","Director", 6700),
    Empleado("Ana","Presidenta", 7500),
    Empleado("Antonio","Administrativo", 2100),
    Empleado("Sara","Secretaria", 2150),
    Empleado("Mario","Botones", 1800),
]

# Funcion de calculo de comision agregandole un porcentaje
def calculo_comision(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado


listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)