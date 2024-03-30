precios = {
    ' Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral):
    # Código SIN List Comprehension
    """
    filtro = {}
    for clave, valor in diccionario.items():
        if valor > umbral:
            filtro[clave] = valor
    """
    # Código CON List Comprehension
    return {clave: valor for clave, valor in diccionario.items() if valor > umbral}

print(filtrar(precios, 12000))