colores = [' verde', '  rojo', '  rosa', 'azul']
colores = [color.strip() for color in colores]
print(colores)

colores.append('celeste')
print(colores)

colores.pop(3)
print(colores)

color = colores.pop(0)
print(color)
print(colores)

colores.remove('rojo')
print(colores)

# colores.remove('azul') # ValueError. El elemento ya no existe
colores.append('amarillo')
colores.append('celeste')
print(colores)

colores.remove('celeste')
print(colores)