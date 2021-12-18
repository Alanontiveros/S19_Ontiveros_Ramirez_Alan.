"""
Date:       2021-12-18
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T4E1_rock_paper.py
Brief:      El programa se ejecuta hasta que alguien gane dos de tres partidas.
            para abreviar las entradas se utilizan las iniciales en ingles.
            r = piedra
            p = papel
            s = tijeras
Score:      -
Version:    0.0.1
Fixies:     -
"""
import random


def juego():
    user = input("que eliges? 'r' para piedra, 'p' para papel, 's' para tijeras\n")
    user = user.lower()  # Convierte mayusculas a minusculas

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 0, user, computer

    # r > s, s > p, p > r
    if ganaste(user, computer):
        return 1, user, computer

    return -1, user, computer


def ganaste(jugador, oponente):
    # retorna verdadero cuando gana jugador
    # condiciones para ganar r > s, s > p, p > r
    if (jugador == 'r' and oponente == 's') or (jugador == 's' and oponente == 'p') \
            or (jugador == 'p' and oponente == 'r'):
        return True
    return False


def ganar_dos_de_tres(n):
    # El juego se ejecuta hasta que alguien gane 2 de 3
    victorias_user = 0
    victorias_computer = 0
    victorias_necesarias = (3 / 2)
    while victorias_user < victorias_necesarias and victorias_computer < victorias_necesarias:
        resultado, user, computer = juego()
        # el empate se calcula así:
        if resultado == 0:
            print('¡Empate! la computadora y tú eligieron la misma opción. \n'.format(user))
        # la victoria se calcula así:
        elif resultado == 1:
            victorias_user += 1
            print('Escogiste {} y la computadora escogio {}. tu ganas!\n'.format(user, computer))
        else:
            victorias_computer += 1
            print('Escogiste {} y la computadora escogio {}. tu perdiste :(\n'.format(user, computer))

    if victorias_user > victorias_computer:
        print('ganaste 2 de {} juegos!  :D'.format(n))
    else:
        print('la computadora gano 2 de {} juegos. suerte a la proxima!'.format(n))


if __name__ == '__main__':
    ganar_dos_de_tres(3)
