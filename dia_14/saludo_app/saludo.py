def saludar(nombre):
    print(f'Hola {nombre}')
    
if __name__ == '__main__':
    from sys import argv
    saludar(argv[1])