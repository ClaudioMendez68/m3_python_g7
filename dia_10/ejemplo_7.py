diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33 , "altura": 1.55}
diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta"}

diccionario_a.update(diccionario_b)
print(diccionario_a)
# print(diccionario_b)

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33 , "altura": 1.55}
diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta", "altura": 155}

diccionario_a.update(diccionario_b)
print(diccionario_a)

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33 , "altura": 1.55}
diccionario_b = {"mascota": "miti", "ejercicio": "bicicleta", "altura": 155}

diccionario_b.update(diccionario_a)
print(diccionario_b)