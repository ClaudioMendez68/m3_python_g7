valores = [0, 4, 5, 6, 7, 8, 9]
lista = []

for valor in valores:
    if valor % 2 == 0:
        lista.append ('Divisible')
    else:
        lista.append ('No Divisible')
        
lista2 = ['Divisible' if valor  % 2 == 0 else 'No Divisible' for valor in valores]
print(lista)
print(lista2)