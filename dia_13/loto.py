from random import choice

"""
pool = []
for n in range(1, 42):
    pool.append(n)
"""
pool = [n for n in range(1, 42)]

def sacar_numero(posicion):
    global pool
    # print(pool)
    elegido = choice(pool)
    pool.remove(elegido)
    if posicion == 'septimo':
        print(f'El Comodín es: {elegido}')
    else:
        print(f'El {posicion} número es: {elegido}')

sacar_numero('primer')
sacar_numero('segundo')
sacar_numero('tercer')
sacar_numero('cuarto')
sacar_numero('quinto')
sacar_numero('sexto')
sacar_numero('septimo')
print('Sorteo Terminado')