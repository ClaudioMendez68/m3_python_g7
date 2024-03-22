prefijo = ['La', 'El', 'La', 'El']
frutas = ['manzana', 'plátano', 'frutilla', 'tomate']
colores = ['verde', 'amarillo', 'roja', 'rojo']

for pref, fruta, color in zip(prefijo, frutas, colores):
    print(f'{pref} {fruta} es {color}')
    
