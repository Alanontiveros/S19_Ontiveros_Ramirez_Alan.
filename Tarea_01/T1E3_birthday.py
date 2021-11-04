"""Ingresar tu fecha de cumpleaños como enteros en variables por separado
e imprímela junto al string:
“Year: xxxx - Month: xx - Day: xx”
donde las xx son las variables correspondientes."""
#Dia
var_año = int(input("Introduce el año en que naciste:"))
var_mes = int(input("Introduce el mes en que naciste:"))
var_dia = int(input("Introduce el dia en que naciste:"))

print(f" Year: - {var_año} Month: - {var_mes:02d} day: - {var_dia:02d}")

