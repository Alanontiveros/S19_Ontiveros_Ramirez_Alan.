"""
Date:       2021-11-18
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T3E3_arithmetic.py
Brief:      Se crearon funciones para realizar operaciones de :
            suma, resta, multiplicacion y division. al iniciar el codigo
            se solicitará que operación se desea realizar.
Score:      -
Version:    0.0.1
Fixies:     -
"""

if __name__ == '__main__':
    def f_suma():
        num_1 = float(input('Ingresa el primer numero: '))
        num_2 = float(input('Ingresa el segundo numero: '))
        result = num_1 + num_2
        return 'El resultado es: {}'.format(result)

    def f_resta():
        num_1 = float(input('Ingresa el primer numero: '))
        num_2 = float(input('Ingresa el segundo numero: '))
        result = num_1 - num_2
        return 'El resultado es: {}'.format(result)

    def f_multiplicar():
        num_1 = float(input('Ingresa el primer numero: '))
        num_2 = float(input('Ingresa el segundo numero: '))
        result = num_1 * num_2
        return 'El resultado es: {}'.format(result)

    def f_dividir():
        num_1 = float(input('Ingresa el primer numero: '))
        num_2 = float(input('Ingresa el segundo numero: '))
        result = num_1 / num_2
        return 'El resultado es: {}'.format(result)

while True:
    print('Opción 1 suma')
    print('Opción 2 resta')
    print('Opción 3 multiplicación')
    print('Opción 4 división')
    print('Opción 5 terminar')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(f_suma())
        elif opcion == 2:
            print(f_resta())
        elif opcion == 3:
            print(f_multiplicar())
        elif opcion == 4:
            print(f_dividir())
        elif opcion == 5:
            print('fin del programa')
            break
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo datos correctos: ')
