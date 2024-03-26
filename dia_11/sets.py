muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

for elemento in muchos_animales:
    print(elemento)

muchos_animales.add('Chancho')
muchos_animales.remove('Gato')
muchos_animales.discard('Leon')
eliminado = muchos_animales.pop()
print(eliminado)
muchos_animales.clear()

print(muchos_animales.__dir__())
print(muchos_animales.__dir__)