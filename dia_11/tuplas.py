tupla1 = (1, 3, 5, 7, 9)
print(tupla1[1])
print(type(tupla1))

for num in tupla1:
    print(num)

tupla2 = ('nombre', 'Claudio')
print(tupla2)
nom, text = tupla2
print(nom)
print(text)
# tupla2[2] = 'Méndez'

dicc1 = list({"nota1":5,"nota2":6}.items())
print(dicc1)#[('nota1', 5), ('nota2', 6)]
print(dicc1[0])

""" tupla_ej = ('Abril', 2021)
print(tupla_ej)
print(type(tupla_ej))

month, year = tupla_ej # Desempaquetado de los elementos de la tupla
print(tupla_ej)
print(month, year)
print(*tupla_ej) # También se puede desempaquetar con el uso de '*': *tupla """