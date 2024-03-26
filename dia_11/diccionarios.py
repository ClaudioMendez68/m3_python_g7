from os import system

computador = {"notebook": 489990 , "tablet": 120000 , "cargador": 12400}
print(computador)
print(computador.keys())
print(computador.values())
print(computador.items())

system('cls')

print(computador.get('notebook', 'No se encuentra el elemento solicitado'))
print(computador.get('celular', 'No se encuentra el elemento solicitado'))