from math import  sqrt

g = float(input("Ingrese la constante gravitacional del planeta en [m/s2]: "))
radio = float(input("Ingrese el radio del planeta en [Kms]: "))

v_esc = sqrt(2*g*radio*1000)

print (f"La velocidad de escape del planeta es: {round(v_esc, 1)} [m/s]")