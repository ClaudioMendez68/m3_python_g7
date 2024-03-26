from os import system

diccionario = {'k1': 5, 'k2': 7}
conv_lista = list(diccionario.items())
print(diccionario)
print(conv_lista)

conv_diccionario = dict(conv_lista)
print(conv_diccionario)

# system('cls')

tupla_ej = ('Abril', 2021)
conv_set = set(tupla_ej)
print(tupla_ej)
print(conv_set)

conv_tupla = tuple(conv_set)
print(conv_tupla)