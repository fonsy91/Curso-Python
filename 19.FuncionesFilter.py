'''
Funciones filter: verifica que los elementos de una secuencia cumplen una 
condicion, devolviendo un iterador con los elementos que cumplen dicha 
condicion
'''

# CLASE
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} euros".format(self.nombre, self.cargo, self.salario)

# Determinar que numeros son pares y cuales no y quiero 
# que me devuelva los numeros pares

def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17,24,39,8,51,92]

print(list(filter(numero_par,numeros)))

# Podemos hacer todo esto con funciones lambda
print(list(filter(lambda numero_par: numero_par%2 == 0,numeros)))

# Normalmente utilizamos filter para filtrar objetos
listaEmpleados = [
    Empleado("Juan","Director", 75000),
    Empleado("Ana","Presidenta", 85000),
    Empleado("Antonio","Administrativo", 25000),
    Empleado("Sara","Secretaria", 27000),
    Empleado("Mario","Botones", 21000),
]

# Hacemos un filter para los salarios mayores de 50000
salarios_Altos = filter(lambda empleado: empleado.salario > 50000, listaEmpleados)

for empleado_salario in salarios_Altos:
    print(empleado_salario)