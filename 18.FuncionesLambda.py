'''
Las funciones lambda consiste en resumir una funcion normal
en una expresion lambda (mas corta)
'''

# Funcion del area de un triangulo
def area_triangulo(base, altura):
    return (base*altura)/2

# Simplificamos esta funcion con una funcion lambda
areaTriangulo = lambda base, altura: (base*altura)/2
print(area_triangulo(7,5))

al_cubo = lambda numero: pow(numero,3)
print(al_cubo(2))

destacarValor = lambda comision: "¡{}! euros".format(comision)
comisionAna = 14555
print(destacarValor(comisionAna))