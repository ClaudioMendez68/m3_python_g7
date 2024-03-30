def get_multiple(diccionario, *claves):
    # Código SIN List Comprehension
    """
    result = {}
    for clave in claves:
        result[clave] = diccionario[clave]    
    return result
    """
    return {clave: diccionario[clave] for clave in claves}

diccionario_prueba = {'manzana': 'verde', 
                    'platano': 'amarillo',
                    'frutilla': 'roja'}

resultado = get_multiple(diccionario_prueba, 'manzana', 'platano')
print(resultado)