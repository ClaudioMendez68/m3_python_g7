numeros = [100 , 20 , 70 , 500]
animales = ["perro", "gato", "hurón", "erizo"]

numeros.reverse()
print(numeros)
animales.reverse()
print(animales)

print(animales.index('gato'))
print(numeros.index(500))

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semana.sort()
print(semana)

animales.sort()
print(animales)
numeros.sort()
print(numeros)

numeros2 = [3, 6, 7, 4, 1]
sorted(numeros2)
print(numeros2)
print(sorted(numeros2))
print(sorted(numeros2, reverse = True))