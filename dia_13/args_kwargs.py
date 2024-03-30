def funcion_args(*args):
    print(type(args))
    return args

output = funcion_args(1, [2, 3], 'hola', {'clave': [4]})
print(output)

print("=========================================================")

def funcion_kwargs(**kwargs):
    print(type(kwargs))
    return kwargs

output2 = funcion_kwargs(valor = 1, Texto = 'hola', lista_notas = [4, 5, 6, 7])
print(output2)