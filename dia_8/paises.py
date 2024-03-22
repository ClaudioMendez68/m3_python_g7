paises = ['México', 'Chile', 'Argentina']
usuarios = [70, 50, 55]
diccionario = {}

for pais, usuario in zip(paises, usuarios):
    diccionario[pais] =  usuario    
print(diccionario)

diccionario2 = {pais:usuario for pais, usuario in zip(paises, usuarios)}
print(diccionario2)

filtro =[]
for pais, usuario in diccionario.items():
    if usuario < 60:
        filtro.append(pais)
print(filtro)

filtro2 = [pais for pais, usuario in diccionario2.items() if usuario < 60]
print(filtro2)