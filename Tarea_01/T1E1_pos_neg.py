"""
Date:       2021-11-04
Author:     Alan Ontiveros Ramirez
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar si es un número positivo, negativo o cero
Score:      100
Version:    1.1.1
Fixes:      -
"""

if __name__ == '__main__':
    num = int(input("ingresa un numero\n"))     # Como solo les dije que ingresaran un número y no les dije
                                                # de que tipo lo mejor es castear a float para que el usuario
                                                # pueda ingresar el número que quiera aun con decimales y si no los
                                                # pone aun asi les respeta el valor entero
    if num == 0:
        print("el numero " + str(num) + " es nulo ")
    else:
        if num > 0: # Si es > 0 es positivo, si es < 0 es negativo, de lo contrario es nulo
            print("el numero " + str(num) + " es positivo")
        else:
            print("el numero " + str(num) + " es negativo")

    # OTRA FORMA DE HACERLO: es como te lo comento abajo con elif y nos ahorramos algunas lineas y es más legible
    # num = float(input("Ingresa un numero: "))
    # if num == 0:
    #     print("el numero " + str(num) + " es nulo ")
    # elif num > 0: # Si es > 0 es positivo, si es < 0 es negativo, de lo contrario es nulo
    #     print("el numero " + str(num) + " es positivo")
    # else:
    #     print("el numero " + str(num) + " es negativo")
