from os import system

mascota = {
    "nombre":"",
    "raza":"",
    "peso":0.0,
    "chip": False,
}

#Recorrer un diccionario default
""" for key in mascota.keys():
    #print(clave)
    mascota[key] = input(f" ingrese {key} de su mascota: ")
    
print(mascota) """

mascota = {key:input (f" ingrese {key} de su mascota: ") for key in mascota.keys()}
print(mascota)

""" for valor in mascota.values():
    print(valor)
    
for k, v in mascota.items():
    print(f"Clave: {k} - Valor: {v}") """