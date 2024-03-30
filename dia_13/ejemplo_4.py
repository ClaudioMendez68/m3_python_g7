def elevar(base, exponente, redondear = False):
    if redondear:
        valor = round(base**exponente, 2)
    else:
        valor = base**exponente
        
    return valor

print(elevar(2.7, 3))
print(elevar(2.7, 3, redondear = True))