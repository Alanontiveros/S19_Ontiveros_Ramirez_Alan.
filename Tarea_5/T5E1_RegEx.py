"""
Date:       2021-12-22
Authors:    Alan Emmanuel Ontiveros Ramírez
            Paulina Alejandra Aguilar Hernandez
File:       T5E1_RegEx.py
Brief:      En este archivo se llaman las funciones creadas en functions.py.
Score:      -
Version:    0.0.1
Fixies:     -
"""

from regex.functions import *

if __name__ == "__main__":

    e_mail1 = input("Correo 1: ")
    e_mail2 = input("Correo 2: ")
    e_mail3 = input("Correo 3: ")
    e_mail4 = input("Correo 4: ")
    check_mail(e_mail1, e_mail2, e_mail3, e_mail4)

    tel_1 = input("telefono 1: ")
    tel_2 = input("telefono 2: ")
    tel_3 = input("telefono 3: ")
    tel_4 = input("telefono 4: ")
    check_numberphone(tel_1, tel_2, tel_3, tel_4)

    curp_1 = input("curp 1: ")
    curp_2 = input("curp 2: ")
    curp_3 = input("curp 3: ")
    curp_4 = input("curp 4: ")
    check_curp(curp_1, curp_2, curp_3, curp_4)
