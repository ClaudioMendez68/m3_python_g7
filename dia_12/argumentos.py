from sys import argv

nombre = argv[1]
apellido = argv[2]

print(f'Mi nombre es {nombre}')
print(f'Mi apellido es {apellido}')
print(f'El nombre de este archivo es: "{argv[0]}"')

print(type(argv))