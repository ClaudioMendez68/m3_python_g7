def tomar_datos():
    """ Solicita ingreso de 2 números y los almacena

    Returns:
        tuple: números capturados
    """
    x = int(input('Ingrese el primer número: '))
    y = int(input('Ingrese el segundo número: '))
    
    return x, y

if __name__ == '__main__':
    print("Probando método tomar_datos()")
    print(tomar_datos())