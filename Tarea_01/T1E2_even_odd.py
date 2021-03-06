"""
Date:       2021-11-04
Author:     Alan Ontiveros Ramirez
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar.
Score:      90
Version:    1.1.1
Fixes:      - PEP8 recomienda no rebasar los 99 carácteres en una línea 
                de código, yo establecí en los requerimientos máximo 72
                carácteres
"""

if __name__ == '__main__':
    num = input("Introduce un número: ")
    num = int(num)  # Excelente, en este caso si tenemos que castear a int, de otra forma no funciona el operador %     # PEP8
    if num == 0:
        print("Este número es nulo.")
    elif num % 2 == 0:  # esta linea divide entre dos y retorna el residuo si es igual a 0 es par de lo contrario impar # PEP8
        print("Este numero es par")
    else:
        print("Este numero es impar")
        
