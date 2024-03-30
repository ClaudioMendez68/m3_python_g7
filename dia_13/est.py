from math import sqrt

def media(lista):
    return sum(lista)/len(lista)

def sdd(lista, media):
    # Código alternativo:
    """ diff = []
    for elemento in lista:
        diff.append((elemento - media)**2 ) """
    
    diff = [(elemento-media)**2 for elemento in lista]    
    return sqrt(sum(diff)/(len(lista)-1))

def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = []
    # Código alternatiivo:
    """ for valor in lista:
        lista_estandarizada.append((valor - m)/sd) """

    lista_estandarizada = [(valor - m)/sd for valor in lista]
    return m, sd, lista_estandarizada

lista = [1, 2, 3, 4, 5, 6]

med, desv_standard, list_std = resultado(lista)

print(f"La media es: {med}")
print(f"La desviación estándar es: {desv_standard}")
print(f"Lista estandarizada: {list_std}")