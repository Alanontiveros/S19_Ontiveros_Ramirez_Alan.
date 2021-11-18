"""
Date:       2021-11-15
Authors:    Alan Emmanuel Ontiveros Ramírez
File:       T2E1_test_list
Brief:      Crear una lista de n elementos de texto (strings) predefinidos, después realizar los
            siguientes pasos (comentar el número y nombre del paso) e imprimir la lista en cada paso:
Score:      -
Version:    0.0.1
Fixies:     -
"""
if __name__ == '__main__':

    my_list = ["Alfa", "Beta", "Gamma", "Delta", "Épsilon"]
    print(my_list)

# 1 Metodo Append
my_list = ["Alfa", "Beta", "Gamma", "Delta", "Épsilon"]
my_list.append("Dseta")
print(my_list)

# 2 Metodo Insert
my_list = ["Alfa", "Gamma", "Delta", "Épsilon"]
my_list.insert(1, "Beta")
print(my_list)

# 3 Metodo Pop
my_list = ["Alfa", "Beta", "Gamma", "Delta", "Épsilon"]
my_list.pop(0)
print(my_list)

# 4 Ordenar los elementos de la A a la Z
my_list = ["Delta", "Épsilon", "Alfa", "Gama", "Beta"]
my_list.sort()
print(my_list)

# 5 Ordenar los elementos de la Z a la A
my_list = ["Delta", "Épsilon", "Alfa", "Gama", "Beta"]
my_list.sort(reverse=True)
print(my_list)
