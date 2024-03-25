animales = ['Gato', 'Perro', 'Tortuga']
animales_2 = ['Hurón', 'Hamster', 'Erizo de Tierra']

print(animales)
print(len(animales))
print(animales_2)
print(len(animales_2))

mascotas = animales + animales_2

print(mascotas)
print(len(mascotas))

animales_actualizados = animales * 4
print(animales_actualizados)
print(len(animales_actualizados))

mascotas = animales_actualizados + animales_2
print(mascotas)
print(len(mascotas))