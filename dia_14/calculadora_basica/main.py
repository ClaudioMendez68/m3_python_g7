import suma
import resta as r
from input import tomar_datos

opcion = input("""Esto es una calculadora:
¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """)

if opcion == '1':
    x, y = tomar_datos()
    suma.sumar(x, y)
elif opcion == '2':
    x, y = tomar_datos()
    r.restar(x, y)
elif opcion == '0':
    print('Nos vemos a la próxima')
else:
    print('NO existe esta Operación')