##Ingresar un número y validar si es un número positivo, negativo o cero

num = int(input("ingresa un numero\n"))
if num == 0:
    print("el numero " + str(num) + " es nulo ")
else:
    if num > 0: # Si es > 0 es positivo, si es < 0 es negativo, de lo contrario es nulo
        print("el numero " + str(num) + " es positivo")
    else:
        print("el numero " + str(num) + " es negativo")
