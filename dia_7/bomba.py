import sys, time

i= int(sys.argv[1])

while i > 0:
    print(f"Autodestrucción en: {i}")
    time.sleep(1)
    i-= 1
    
print("¡¡PUUUMMM!!")