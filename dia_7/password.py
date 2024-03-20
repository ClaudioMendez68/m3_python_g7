import getpass

password= getpass.getpass("Ingrese la clave secreta: ")
while password != "Hola Mundo":
    password= getpass.getpass("Clave INCORRECTA. Ingrese la clave secreta: ")
    
print("La clave es CORRECTA. Bienvenido")