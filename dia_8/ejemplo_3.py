texto = "Claudio Méndez"
for posicion, letra in enumerate(texto):
    print(f"La letra en la posición {posicion} es la {letra}")
    
print("=================================================")

for letra in enumerate(texto):
    print(letra)
    
print(("==============================================="))    
    
diccionario = {
    "Nombre" : "Carlos",
    "Apellido" : "Santana",
    "Ocupación" : "Guitarrista"
}

for clave, valor in enumerate(diccionario):
    print(f"El valor en la posición {clave} es {valor}")