'''
EXCEPCIONES

Se utilizan para capturar los errores tanto logicos como de 
programa, como puede ser una divison entre cero.

'''

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operacion erronea"
    
def divideCompleta():
    try:
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        print("La division es: " + str(op1/op2))

    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero!")
    finally:
        # Lo que va dentro del finally se ejecuta siempre
        print("Calculo finalizado")

divideCompleta()

def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        print("Eres muy joven")
    if edad < 40:
        print("Eres joven")
    if edad < 65:
        print("Eres maduro")
    elif edad < 100:
        print("Cuidate")

print(evaluaEdad(20))
