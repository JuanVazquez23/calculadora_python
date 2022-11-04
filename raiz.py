import math

def raizCuadrada(numero):
    numero = -1
    try:
        numero = math.sqrt(numero)
    except ValueError:
        print("no se puede hacer al raiz de un numero negativo")

    return numero

def division(numero1, numero2):
    try:
        numero = numero1/numero2
    except ZeroDivisionError:
        print("intentaste dividir por 0")

    return numero