##Ingresar un número y validar si es par o impar.

# Excelente, en este caso si tenemos que castear a int, de otra forma no funciona el operador %
num = input("Introduce un número: ")
num = int(num)
if num == 0:
    print("Este número es nulo.")
elif num % 2 == 0: # esta linea divide entre dos y retorna el residuo si es igual a 0 es par de lo contrario impar
    print("Este numero es par")
else:
    print("Este numero es impar")
