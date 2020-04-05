
def divide():

    try:
        op1 = (float(input("Primer número: ")))
        op2 = (float(input("Segundo número: ")))

        print("La division es: " + str(op1/op2))
    except ValueError:
        print("No es un número")
    except ZeroDivisionError:
        print("División entre cero no válida")

    print("Cálculo finalizado")

divide()
