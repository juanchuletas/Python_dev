import math

# Uso de excepciones: Manejando errores en tiempo de ejecucion
# lanzamiento de excepcion
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No existen edades negativas")
    elif edad<20:
        print("Eres muy joven")
    elif edad<40:
        print("Eres joven")
    elif edad<65:
        print("Eres maduro")
    elif edad<100:
        print("Estás por morir")

def obtenraiz(num1):
    if num1<0:
        raise ValueError("No puedes usar negativos")
    else:
        return math.sqrt(num1)

val1 = (int(input("Introduce un número: ")))

try:
    print(obtenraiz(val1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)



evaluaEdad(int(input("Ingresa tu edad: ")))


