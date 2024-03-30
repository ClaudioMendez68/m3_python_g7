def extremo_multiplicado(lista, factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo

print(extremo_multiplicado([1, 2, 3, 4], 4))
print(extremo_multiplicado(lista = [1, 2, 3, 4], factor = 4))