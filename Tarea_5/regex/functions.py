"""
Date:       2021-12-
Authors:    Alan Emmanuel Ontiveros Ramírez
File:
Brief:
Score:      -
Version:    0.0.1
Fixies:     -
"""

import re


def check_mail(e_mail1, e_mail2, e_mail3, e_mail4):
    """
    Esta función busca coincidencias de acuerdo a un parametro especificado con regex '^ $'
    se añade .lower para convertir mayusculas a minusculas en caso de encontrarlas.
    Se busca cumplir con lo siguiente:
    Con expresiones regulares realizar las siguientes validaciones ya sea en forma de
    función o método; mandando a llamar en la condición de main 2 validos y 2
    inválidos para cada caso (los validos retornan True y los inválidos False), añadiendo
    capturas en el archivo README.MD:
    """

    if re.match('^[(a-z0-9\-._)]+@[(a-z0-9\-._)]+\.[(a-z)]{2,15}$', e_mail1.lower()):

        print("Correo correcto")
    else:
        print("Correo incorrecto")

    if re.match('^[(a-z0-9\-._)]+@[(a-z0-9\-._)]+\.[(a-z)]{2,15}$', e_mail2.lower()):

        print("Correo correcto")
    else:
        print("Correo incorrecto")

    if re.match('^[(a-z0-9\-._)]+@[(a-z0-9\-._)]+\.[(a-z)]{2,15}$', e_mail3.lower()):

        print("Correo correcto")
    else:
        print("Correo incorrecto")

    if re.match('^[(a-z0-9\-._)]+@[(a-z0-9\-._)]+\.[(a-z)]{2,15}$', e_mail4.lower()):

        print("Correo correcto")
    else:
        print("Correo incorrecto")


def check_numberphone(tel_1, tel_2, tel_3, tel_4):
    """
    Establecemos un parametro en regex y buscamos la coincidencia.
    Se busca cumplir con lo siguiente:
    Con expresiones regulares realizar las siguientes validaciones ya sea en forma de
    función o método; mandando a llamar en la condición de main 2 validos y 2
    inválidos para cada caso (los validos retornan True y los inválidos False), añadiendo
    capturas en el archivo README.MD:
    """

    pattern = r"[\(?0-9\)?\s?\-?]{1,12}"

    if re.match(pattern, tel_1):
        print("Numero de telefono correcto")
    else:
        print("Numero de telefono incorrecto")

    if re.match(pattern, tel_2):
        print("Numero de telefono correcto")
    else:
        print("Numero de telefono incorrecto")

    if re.match(pattern, tel_3):
        print("Numero de telefono correcto")
    else:
        print("Numero de telefono incorrecto")

    if re.match(pattern, tel_4):
        print("Numero de telefono correcto")
    else:
        print("Numero de telefono incorrecto")


def check_curp(curp_1, curp_2, curp_3, curp_4):
    """
    En esta función no se logro acortar el string para definir el parametro de CURP
    al igual que las funciones anteriores busca las coincidencias en base a el patron regex establecido.
    Se busca cumplir con lo siguiente:
    Con expresiones regulares realizar las siguientes validaciones ya sea en forma de
    función o método; mandando a llamar en la condición de main 2 validos y 2
    inválidos para cada caso (los validos retornan True y los inválidos False), añadiendo
    capturas en el archivo README.MD:
    """

    pattern = r"[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$"

    if re.match(pattern, curp_1):
        print("Curp correcto")
    else:
        print("Curp incorrecto")

    if re.match(pattern, curp_2):
        print("Curp correcto")
    else:
        print("Curp incorrecto")

    if re.match(pattern, curp_3):
        print("Curp correcto")
    else:
        print("Curp incorrecto")

    if re.match(pattern, curp_4):
        print("Curp correcto")
    else:
        print("Curp incorrecto")
