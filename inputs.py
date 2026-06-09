from validaciones import (
    validar_caracteres_flotantes,
    validar_puntos,
    validar_longitud_minima,
    validar_numeros_negativos,
    validar_inicio_fin,
    validar_rango,
    validar_lista
)

# INGRESO DE DATOS NUMERICOS
#ESTO DEBERIA FORMAR PARTE DE LA DOCUMENTACION DE LA FUNCIÓN?
'''
    - Que el ingreso no esté vacío.
    - Que contenga solo caracteres numéricos.
    - Que tenga como máximo un punto decimal.
    - Que no sea negativo.
    - Que no comience ni termine con un punto.
    - Que se encuentre dentro del rango indicado.
'''

def pedir_numero(mensaje:str, minimo:float, maximo:float) -> float:
    """Solicita un número y valida que sea un valor numérico dentro del rango indicado.

    Args:
        mensaje (str): Texto que se mostrará al usuario para solicitar el dato.
        minimo (float): Valor mínimo permitido.
        maximo (float): Valor máximo permitido.

    Returns:
        float: Número validado dentro del rango especificado.
    """

    numero = input(mensaje)
    ingreso_valido = False

    while ingreso_valido == False:

        bandera_validada = True

        if validar_longitud_minima(numero,1) == False:
            print("NO PUEDE ESTAR VACIO")
            bandera_validada = False
        
        if validar_caracteres_flotantes(numero) == False:
            print("SE DEBEN INGRESAR NUMEROS")
            bandera_validada = False

        if validar_puntos(numero) == False:
            print("MAS DE UN PUNTO DECIMAL")
            bandera_validada = False
        
        if validar_numeros_negativos(numero) == False:
            print("FUERA DE RANGO, NO SE PERMITEN NEGATIVOS")
            bandera_validada = False
        
        if validar_inicio_fin(numero) == False:
            print("FORMATO INCORRECTO")
            bandera_validada = False

        if bandera_validada and validar_rango (numero,minimo,maximo) == False:
            print(f"FUERA DE RANGO.({minimo}/{maximo})")
            bandera_validada = False
        
        if bandera_validada:
            ingreso_valido = True
        else:
            print("-----------INVALIDO-----------")
            numero = input("Reingrese un número válido: ")

    return float(numero)

# INGRESO DE OPCIONES CERRADAS 
def pedir_opcion (mensaje:str,opciones:list) -> str: 
    """Solicita al usuario el ingreso de una opción y repite la petición de forma iterativa hasta que el valor ingresado 
    sea una opción válida.

    Args:
        mensaje (str): Mensaje indicativo que se le muestra al usuario para solicitar el dato.
        opciones (list): Conjunto cerrado de valores strings permitidos 

    Returns:
        str: La opción validada que coincide con uno de los elementos de la lista.
    """

    opcion = input(mensaje)

    while validar_lista(opcion, opciones) == False:

        print("INVÁLIDA")

        opcion = input(f"Re{mensaje}")

    return opcion
