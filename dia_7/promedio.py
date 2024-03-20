cant_notas= int(input("¿Cuántas notas quiere promediar?: "))
i = 1 # 0,1,2
suma_notas = 0
while i <= cant_notas:
    nota = float(input(f"Ingresa la nota n° {i}: "))
    suma_notas = suma_notas + nota
    i += 1

print(f"El promedio de notas es: {round(suma_notas/cant_notas, 2)}")