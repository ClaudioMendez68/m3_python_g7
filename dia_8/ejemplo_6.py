prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']

for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')
    
print("=================================================")
    
numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]

for numero in numeros:
    print(numero)
    if numero == "5":
        break
print("Fuera del ciclo FOR")