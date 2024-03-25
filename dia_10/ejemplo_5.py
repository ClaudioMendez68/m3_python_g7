lista = [25, 31, 'hola']
print(lista[2])

diccionario = {'a': 25, 'b':  31, 'c': 'hola'}
print(diccionario['c'])

nums = {1: 'uno',
        'dos': 2}
print(nums)
print(nums[1])
# print(nums[2]) # KeyError: 2

notas = {"Camila": 7 , "Antonio": 5 , "Felipe": 6 , "Antonia": 7}
print(notas['Felipe'])
# print(notas['felipe'])

notas2 = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"Daniela": 7
}

# notas2 = {} # Diccionario vacío
print(len(notas2))
print(notas2)

""" duplicados = {'clave': 1, 'clave': 2}
print(duplicados)

diccionario2 = {'llave 1': 5}
print(diccionario2)
diccionario2['llave 2'] = 9
print(diccionario2)

diccionario2['llave 2'] = 7
print(diccionario2) """