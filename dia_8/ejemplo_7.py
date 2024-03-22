lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
count_str = 0
lista_str = []
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)

print(count_str)
print(lista_str)

lst_str = [elemento for elemento in lista if type(elemento) is str ]

print(lst_str)