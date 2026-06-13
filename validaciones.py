#El sistema deberá validar datos numéricos, aceptando valores que representen correctamente números enteros o decimales (flotantes) dentro de un rango permitido. 
def validar_caracteres_flotantes(texto:str)->bool:
    """Valida que una cadena contenga únicamente caracteres válidos para un número.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si la cadena contiene solo dígitos, punto decimal o signo negativo,
        False en caso contrario.
    """

    retorno = True

    for c in texto:

        if not ("0" <= c <= "9") and c != "." and c != "-":
            retorno = False

    return retorno

def validar_puntos(texto:str) -> bool:
    """Valida que una cadena contenga como máximo un punto decimal.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si contiene cero o un punto decimal,
        False si contiene más de uno.
    """

    retorno = True
    cantidad_puntos = 0

    for c in texto: 

        if c == ".":
            cantidad_puntos += 1

    if cantidad_puntos > 1: 
        retorno = False

    return retorno
        
def validar_longitud_minima(cadena:str,minimo:int) -> bool:
    """Valida que una cadena tenga una longitud minima determinada.

    Args:
        cadena (str): Cadena a validar.
        minimo (int): Cantidad mínima de caracteres requerida.

    Returns:
        bool: True si la longitud de la cadena es mayor o igual al mínimo indicado,
        False en caso contrario.
    """

    retorno = False

    if len(cadena) >= minimo :
        retorno = True

    return retorno

def validar_numeros_negativos(texto:str) -> bool:
    """Valida que el número ingresado no sea negativo.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si el número no posee signo negativo al inicio,
        False en caso contrario.
    """

    retorno = True

    if len(texto) > 0 and texto[0] == "-": 
        
        retorno = False    

    return retorno

def validar_inicio_fin(texto:str) -> bool:
    """Valida que una cadena numérica no comience ni termine con un punto decimal.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si el formato es correcto,
        False si comienza o termina con un punto decimal.
    """

    retorno = True

    if len(texto) > 0: 
        if texto[0] == "." or texto[len(texto)-1] == ".": 
            retorno = False
    return retorno

def validar_rango(texto:str, valor_minimo:float, valor_maximo:float) -> bool:
    """Valida que un número se encuentre dentro de un rango determinado.

    Args:
        texto (str): Número a validar en formato texto.
        valor_minimo (float): Valor mínimo permitido.
        valor_maximo (float): Valor máximo permitido.

    Returns:
        bool: True si el número se encuentra dentro del rango indicado,
        False en caso contrario.
    """

    retorno = True
    numero = float(texto)

    if numero < valor_minimo or numero > valor_maximo:
        retorno = False

    return retorno

#El sistema deberá validar opciones cerradas, es decir, valores que solo pueden pertenecer a un conjunto predefinido. 
def validar_lista(texto:str, lista_opciones:list) -> bool:
    """Valida que un texto coincida exactamente con alguna de las opciones permitidas.

    Args:
        texto (str): Cadena ingresada por el usuario a validar.
        lista_opciones (list): Lista de opciones válidas permitidas para el ingreso.

    Returns:
        bool: True si el texto coincide con alguna opción de la lista,
        False en caso contrario.
    """

    retorno = False

    for opcion in lista_opciones:

        if texto == opcion:
            retorno = True

    return retorno

# INGRESO CADENAS
def validar_solo_espacios(texto:str) -> bool:
    """Verifica que la cadena contenga al menos un carácter distinto de espacio.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si existe al menos un carácter distinto de espacio, False si la cadena contiene únicamente espacios.
    """

    retorno = False

    for c in texto:

        if c != " ":
            retorno = True
            break

    return retorno

def validar_texto(texto:str) -> bool:
    """Valida que un texto tenga una longitud mínima y no contenga solo espacios.

    Args:
        texto (str): Cadena a validar.

    Returns:
        bool: True si el texto es válido, False en caso contrario.
    """    

    retorno = True

    if validar_longitud_minima(texto, 5) == False:
        retorno = False

    if validar_solo_espacios(texto) == False:
        retorno = False

    return retorno
