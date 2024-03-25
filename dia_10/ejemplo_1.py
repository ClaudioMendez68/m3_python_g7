from os import system

system('cls')

lista_pares = [2, 4, 6, 8, 10]
lista_vacia = []
print(lista_pares[-1])
# print(lista_vacia[-1])

lista_de_numeros = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9, 10, 13]
backup_lista_de_numeros = lista_de_numeros.copy() # Forma correcta de respaldar una lista
backup_2 = lista_de_numeros[:] # Otra forma de respaldar una lista
backup_3 = lista_de_numeros + []
backup_4 = lista_de_numeros * 1
backup_5 = list(lista_de_numeros)

print(lista_de_numeros.__dir__)
print(lista_de_numeros.__dir__())

lista_de_numeros.insert(15, 20)
print(lista_de_numeros)

lista_eliminados = []
lista_de_numeros.pop()
lista_eliminados.append(lista_de_numeros.pop(-1))

# print(lista_de_numeros.pop(-1))
print(lista_de_numeros)
print(lista_eliminados)
print(backup_lista_de_numeros)
print(backup_5)