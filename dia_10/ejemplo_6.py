diccionario = {"celular": 140000 , "notebook": 489990 , "tablet": 120000 , "cargador": 12400}
print(diccionario)

del(diccionario['celular'])
print(diccionario)

eliminado = diccionario.pop('tablet')
print(eliminado)
print(diccionario)