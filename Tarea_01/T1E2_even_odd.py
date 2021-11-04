##Ingresar un número y validar si es par o impar.

# En el PDF no les puse este requisito, pero en todas las tarea vamos a incluir esta condición
if __name__ == '__main__':
    num = input("Introduce un número: ")
    num = int(num)  # Excelente, en este caso si tenemos que castear a int, de otra forma no funciona el operador %
    if num == 0:
        print("Este número es nulo.")
    elif num % 2 == 0:  # esta linea divide entre dos y retorna el residuo si es igual a 0 es par de lo contrario impar
        print("Este numero es par")
    else:
        print("Este numero es impar")
