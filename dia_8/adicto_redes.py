minutos = [120 , 50 , 600 , 30 , 90 , 10 , 200 , 0 , 500]
resultado = []

for minuto in minutos:
    if minuto < 90:
        resultado.append('Bien')
    else:
        resultado.append('Mal')
        
print(resultado)

output = ['Bien' if minuto < 90 else 'Mal' for minuto in  minutos]

print(output)