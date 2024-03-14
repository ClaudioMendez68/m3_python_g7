p = float(input("Ingrese el precio de la suscripción $: "))
u = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese el gasto total $: "))
util_ant = float(input("Ingrese las utiolidades del año anterior $: "))

utilidad = p*u - gt
ratio = utilidad/util_ant

print(f"La utilidad del período es de ${round(utilidad)}.-")
print(f"El índice de crecimiento de la utilidad respecto del año pasado es de: {round(ratio, 2)}")