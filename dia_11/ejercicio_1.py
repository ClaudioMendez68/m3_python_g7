diccionario = diccionario = {"celular": 140000,
                             "notebook": 489990,
                             "tablet": 120000,
                             "cargador": 12400}

print(diccionario)
diccionario['smartwatch'] = 123000
del diccionario['celular']
diccionario['tablet'] = 148000
eliminado = diccionario.pop('cargador')

print(eliminado)
print(diccionario)