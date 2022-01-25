"""
Date:       2021-11-17
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T2E2_number_list
Brief:      Crear una lista con n números desde el teclado, después
            realizar los pasos requeridos en el correo.
Score:      100
Version:    1.1.1
Fixes:      + Perfecto
"""


if __name__ == '__main__':

    # 1 Imprimir elementos y tipos de la lista.
    print('Instrucciones:')
    print('-Escribre una secuencia de numeros-')
    print('-Separa cada numero usando espacios-')
    print('-Al finalizar presiona enter-')
    numbers_str = input('Escribe tus números: ').split()
    print(numbers_str)
    print(f'tipo de lista es: {type(numbers_str)}')

    # 2. Cambiar el tipo de todos los elementos a int.
    print('Se cambiaron el tipo de todos los elementos a int')
    number = [int(x) for x in numbers_str]
    print(f'Tu lista es : {number}')

    # 3.Imprime través de un valor(es) que se ingrese por el teclado.

    add_num = input('¿Deseas agregar mas numeros? y = sí / n = no : ')
    if add_num == "y":
        numbers_str_add = input('Escribre tus numeros: ').split()
        print(numbers_str_add)
        print(f'tipo de lista es: {type(numbers_str_add)}')
        print('Se cambiaron el tipo de todos los elementos a int')
        print('Tu nueva lista es: ')
        number_add = [int(x) for x in numbers_str_add]
        new_list_num = (number + number_add)
        # 4 ordenar elementos.

        print('Se ordenarón los elementos de forma ascendente')
        new_list_num.sort()
        print(new_list_num)
        # 5 ordenar elementos en reversa.

        print('Se ordenarón los elementos de forma descendente')
        new_list_num.sort(reverse=True)
        print(new_list_num)

    elif add_num == "n":
        print('No se eligieron mas numeros, la lista es:  ')
        print(number)


