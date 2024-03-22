diccionario = {
    "Nombre" : "Carlos",
    "Apellido" : "Santana",
    "Ocupación" : "Guitarrista"
}

for clave in diccionario:
    print(clave)
    
print(("================================"))
    
for clave in diccionario:
    print(diccionario[clave])
    
print("=================================")
    
for clave, valor in diccionario.items():
    print(f"Mi {clave} es {valor}")
    
print("=================================")
    
for par in diccionario.items():
    print(par)
    
print("=================================")
    
for clave in diccionario.keys():
    print(clave)
    
print("=================================")
    
for valor in diccionario.values():
    print(valor)