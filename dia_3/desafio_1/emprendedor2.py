p = float(input("Ingrese el precio de la suscripción $: "))
u_norm = int(input("Ingrese el número de usuarios normales: "))
u_premium = int(input("Ingrese el número de usuarios premium: "))
gt = float(input("Ingrese el gasto total $: "))

utilidad = p*u_norm + 1.5*p*u_premium - gt

print(f"La utilidad del período es de ${round(utilidad)}.-")