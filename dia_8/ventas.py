meses = ['Octubre', 'Noviembre', 'Diciembre']
ventas = [65000, 68000, 72000]
diccionario = {}

# Convertir tablas en diccionario
for mes, venta in zip(meses, ventas):
    diccionario[mes] = venta
print(diccionario)

diccionario2 = {mes:venta for mes, venta in zip(meses, ventas)}
print(diccionario2)

# Modificar diccionario con ventas aumentadas en 10%
for mes, venta in diccionario.items():
    diccionario[mes] = round(venta*1.1)
print(diccionario)

diccionario2 = {mes:round(venta*1.1) for mes, venta in diccionario2.items()}
print(diccionario2)

# Crear nuevo diccionario con ventas disminuidas en 20%
nuevo_diccionario = {}
for mes, venta in diccionario.items():
    nuevo_diccionario[mes] = round(venta*0.8)
print(nuevo_diccionario)

nuevo_diccionario2 = {mes:round((venta*0.8)) for mes, venta in diccionario2.items()}
print(nuevo_diccionario2)