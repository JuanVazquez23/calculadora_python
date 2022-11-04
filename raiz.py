import math


def raizCuadrada(numero):
    return math.sqrt(numero)


def resta(n, m):
    return n - m


try:
    num1 = int(input('Dame un numero: '))
    num2 = int(input('Dame otro numero: '))
except ValueError:
    print('Ingrese dos numeros, por favor.')

operacion = input('Que operacion quiere realizar? ')

match operacion:
    case 'suma':
        suma(num1, num2)
    case 'resta':
        resta(num1, num2)
    case 'multiplicacion':
        multiplicacion(num1, num2)
    case 'division':
        division(num1, num2)
    case 'potencia':
        potencia(num1, num2)
    case 'raiz':
        raiz(num1, num2)
    case other:
        print('No conozco esa operacion :(')
