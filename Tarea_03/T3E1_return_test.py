"""
Date:       2021-11-15
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T2E1_test_list
Brief:      Escribir una función que pida un número y regrese un string (que contenga el número introducido).
Score:      -
Version:    0.0.1
Fixies:     -
"""

if __name__ == '__main__':
    def nombre_edad():

        nombre = input('Ingrese su nombre: ')
        edad = int(input('Ingrese su edad: '))
        return 'Su nombre es {} y tiene {} años de edad'.format(nombre, int(edad))
    print(nombre_edad())
