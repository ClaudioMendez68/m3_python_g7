# Docstring simple
def elevar(base, exponente):
    """ Esta función tiene como objetivo elevar una base a un exponente. """
    return base**exponente

print(elevar(2, 3))

# Docstring recomendado por Google
def elevar2(base, exponente):
    """Esta función tiene como objetivo elevar una base a un exponente.

    Args:
        base ([float]): Base de la potencia.
        exponente ([float]): Exponente de la potencia.

    Returns:
        [float]: Se retorna un float resultante de elevar la base a la Potencia.
    """
    return base**exponente

print(elevar2(3, 3))

# Sphinx
def elevar3(base, exponente):
    """Esta función tiene como objetivo elevar una base a un exponente.
    
    :param base: Corresponde a la base de la Potencia.
    :type base: [float]
    :param exponente: Corresponde al exponente de la Potencia.
    :type exponente: [float]
    :return: Corresponde a la resultante de elevar la base a la Potencia.
    :rtype: [type]
    """
    return base**exponente

print(elevar3(4, 3))

# Docblockr
def elevar4(base, exponente):
    """Esta función tiene como objetivo elevar una base a un exponente.

    Arguments:
        base {[float]} -- Base de la Potencia.
        exponente {[float]} -- Exponente de la Potencia.
    Returns:
        [float] -- Se retorna un float resultante de elevar la base a la Potencia.
    """
    return base**exponente

print(elevar4(5, 3))

# Numpy
def elevar5(base, exponente):
    """Esta función tiene como objetivo elevar una base a un exponente.

    Parameters
    ----------
    base : [float]
        Base de la Potencia.
    exponente : [float]
        Exponente de la Potencia.
        
    Returns
    -------
    [float]
        Retorna el resultado de elevar base a exponente.
    """
    return base**exponente

print(elevar5(6, 3))