"""
Date:       2021-11-18
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T3E2_temperature.py
Brief:      Crear dos funciones para convertir temperatura C° -> f° / f° -> C°
Score:      -
Version:    0.0.1
Fixies:     -
"""

if __name__ == '__main__':
    def fahrenheit_celsius():
        """conversión de grados fahrenheit a grados celsius"""

        fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return '{}° Fahrenheit son {}° Celsius'.format(fahrenheit, int(celsius))


    def celsius_fahrenheit():
        """conversión de grados celsius a fahrenheit"""

        celsius = int(input('Ingrese la temperatura en grados Celsius: '))
        fahrenheit = (celsius * 9) / 5 + 32
        return '{}° Celsius son {}° Fahrenheit'.format(celsius, int(fahrenheit))


    while True:
        print('Teclea 1 si desea convertir grados Fahrenheit a Celsius')
        print('Teclea 2 si desea convertir grados Celsius a Fahrenheit')
        print('Teclea 3 para terminar')

        try:
            opcion = int(input('Seleccione una opción: '))
            if opcion == 1:
                print(fahrenheit_celsius())
            elif opcion == 2:
                print(celsius_fahrenheit())
            elif opcion == 3:
                print('Fin del programa')
                break
            else:
                raise ValueError
        except ValueError:
            print('Ingrese solo datos correctos: ')
