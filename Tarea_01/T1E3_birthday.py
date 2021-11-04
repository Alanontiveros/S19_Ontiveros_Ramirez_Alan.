"""Ingresar tu fecha de cumpleaños como enteros en variables por separado
    e imprímela junto al string:
    “Year: xxxx - Month: xx - Day: xx”
    donde las xx son las variables correspondientes."""

# En el PDF no les puse este requisito (en el correo si), pero en todas las tarea vamos a incluir esta condición
if __name__ == '__main__':
    # Dia
    var_año = int(input("Introduce el año en que naciste:"))
    var_mes = int(input("Introduce el mes en que naciste:"))
    var_dia = int(input("Introduce el dia en que naciste:"))

    # Todo perfecto pero el guion de la impresion va despues del valor
    # print(f" Year: - {var_año} Month: - {var_mes:02d} day: - {var_dia:02d}")
    print(f" Year: {var_año} -  Month: {var_mes:02d} -  day: {var_dia:02d}")
    
