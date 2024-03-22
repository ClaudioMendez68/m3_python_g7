claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]

diccionario2 = {k:v for k,v in zip(claves, valores)}

print(diccionario2)