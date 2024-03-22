segundos = [100 , 50 , 1000 , 5000 , 1000 , 500]
minutos = []

for segundo in segundos:
    minutos.append(int(segundo/60))
    
print(minutos)

minutes = [int(segundo/60) for segundo in segundos]
print(minutes)