p = float(input("Ingrese el precio de la suscripción $: "))
u = int(input("Ingrese el número de usuarios: "))
gt = float(input("Ingrese el gasto total $: "))

utilidad = p*u - gt

print(f"La utilidad del período es de ${round(utilidad)}.-")