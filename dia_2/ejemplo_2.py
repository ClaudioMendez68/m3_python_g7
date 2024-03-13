# la división entre enteros resulta en un float.
# el separador decimal es el punto, no la coma.
print(20+3.5)

# Duplicación en variables del tipo STRING
nombre = "Claudio Méndez "
print(3*nombre)
print(type(nombre))

num = 100
print(3*num)
print(type(num))

#MÉTODOS
#Método .count()
print("==========================================================")
print("Contando cuántas veces se repite un caracter con .count()")
print("Paralelepípedo".count("p"))
print("Paralelepípedo".count("i"))

#Método .upper() y .lower()
print("==========================================================")
print("gaLaga SpAce FiGhter".upper())
print("gaLaga SpAce FiGhter".lower())

# Método .title() y .capitalize()
print("==========================================================")
print("gaLaga SpAce FiGhter".title())
print("gaLaga SpAce FiGhter".capitalize())

# Función len()
print("==========================================================")
print(len("gaLaga SpAce FiGhter"))
# print(len(123456.789)) # ERROR, puesto que un número no tiene largo

# Método .join()
print("==========================================================")
print(", ".join(["a", "b", "c"]))

# Tipo de datos
print("==========================================================")
print("Tipos de variables:")

entero = 7
decimal = 3.14
string = "Claudio Méndez"
booleano = True

print(type(entero)) # <class 'int'>
print(type(decimal)) # <class 'float'>
print(type(string)) # <class 'str'>
print(type(booleano)) # <class 'bool'>

# Precisión de datos
print("==========================================================")
promedio = (4+5+7)/3
print(f"El promedio es: {promedio}")
print(f"El promedio es: {promedio:.4f}")
print(f"El promedio es: {round(promedio, 3)}")

# Ingreso de datos: input()
nombre = input("Ingrese su nombre: ")
print(f"El nombre ingresado es: {nombre}")
edad = input("Ingrese su edad: ")
print(f"La edad ingresada es: {edad} años")